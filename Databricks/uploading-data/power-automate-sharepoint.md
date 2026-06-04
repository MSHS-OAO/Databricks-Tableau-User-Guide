# Power Automate — SharePoint to Databricks

End-to-end event-driven pipeline that uploads SharePoint files to a Databricks Catalog [Volume](../../Common%20Definitions.md#volume) and triggers a [Job](../../Common%20Definitions.md#job) to ingest them into a [Delta Table](../../Common%20Definitions.md#delta-table).

## Architecture

```
SharePoint Document Library
        ↓ (file uploaded)
Power Automate Flow
        ↓ (4 actions)
   1. When a file is created (properties only) — SharePoint trigger
   2. Get file content using path — fetches file bytes
   3. HTTP PUT → Databricks Files API — uploads to Volume
   4. HTTP POST → Databricks Jobs API — triggers ingest job
        ↓
Databricks Job (notebook)
        ↓ (reads Excel, transforms)
Delta Table in Catalog
```

## Prerequisites

- Microsoft 365 account with [Power Automate](../../Common%20Definitions.md#power-automate) access
- Databricks workspace with Catalog enabled
- Workspace admin must enable the `files` API scope for PATs
- [Personal Access Token](../../Common%20Definitions.md#personal-access-token-pat) with both `files` and `jobs` scopes
- Permissions on the target [Volume](../../Common%20Definitions.md#volume) (`WRITE VOLUME`) and [Schema](../../Common%20Definitions.md#schema) (`CREATE TABLE`)

## Setup

### 1. SharePoint

- Site: Balanced Scorecards Automation
- Library: Documents
- Watched folder: `/Shared Documents/DataFeeds`

### 2. Databricks Volume

```
/Volumes/datahub_dev_bronze/scorecards_raw_files/finance/
```

Grant write access if not already granted:

```sql
GRANT WRITE VOLUME ON VOLUME datahub_dev_bronze.scorecards_raw_files.finance
TO `user@mssm.edu`;
```

### 3. Personal Access Token

Databricks workspace → **Settings → Developer → Access Tokens → Generate new token**

Required scopes:
- `files` — to upload to Volumes via REST API
- `jobs` — to trigger job runs via REST API

Without these scopes, requests return `403 Forbidden: required scopes: <scope>`.

## Power Automate Flow

### Action 1: When a file is created (properties only)

| Field | Value |
|---|---|
| Site Address | Balanced Scorecards Automation |
| Library Name | Documents |
| Folder | `/Shared Documents/DataFeeds` |

Avoid the deprecated `When a file is created in a folder` trigger.

### Action 2: Get file content using path

| Field | Value |
|---|---|
| Site Address | (same as above) |
| File Path | `Full path` (dynamic content from trigger) |
| Infer Content Type | **No** |

Setting **Infer Content Type** to **No** is critical for binary files like Excel. When set to `Yes`, Power Automate tries to interpret the file and corrupts the binary content, resulting in a 0-byte file landing in the Volume.

### Action 3: HTTP PUT — Upload to Volume

| Field | Value |
|---|---|
| Method | `PUT` |
| URI | `https://adb-7405606624435497.17.azuredatabricks.net/api/2.0/fs/files/Volumes/datahub_dev_bronze/scorecards_raw_files/finance/@{triggerOutputs()?['body/{FilenameWithExtension}']}` |
| Header: Authorization | `Bearer <PAT>` |
| Header: Content-Type | `application/octet-stream` |
| Body (expression) | `base64ToBinary(body('Get_file_content_using_path')?['$content'])` |

The Body expression is essential. SharePoint hands Power Automate a JSON envelope:

```json
{
  "$content-type": "application/octet-stream",
  "$content": "UEsDBBQABg..."
}
```

The expression extracts the `$content` field and decodes the base64 string back into raw binary, which is what the Databricks Files API expects.

Enter this through the **fx (function)** button — not as plain text — otherwise Power Automate sends the literal string instead of evaluating it.

### Action 4: HTTP POST — Trigger Databricks Job

| Field | Value |
|---|---|
| Method | `POST` |
| URI | `https://adb-7405606624435497.17.azuredatabricks.net/api/2.1/jobs/run-now` |
| Header: Authorization | `Bearer <PAT>` |
| Header: Content-Type | `application/json` |
| Body | See below |

```json
{
  "job_id": 432705911179775,
  "job_parameters": {
    "file_name": "@{triggerOutputs()?['body/{FilenameWithExtension}']}"
  }
}
```

## Databricks Notebook

Path: `/Workspace/Users/user@mssm.edu/bsc_finance_ingest`

```python
dbutils.widgets.text("file_name", "OAO_PRODUCTION_BSC_FINANCE_TABLE.xlsx")
file_name = dbutils.widgets.get("file_name")

volume_path = f"/Volumes/datahub_dev_bronze/scorecards_raw_files/finance/{file_name}"
target_table = "datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw"

print(f"Reading from: {volume_path}")

import pandas as pd
pdf = pd.read_excel(volume_path)
df = spark.createDataFrame(pdf)

# overwriteSchema handles schema evolution when columns change between runs
df.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable(target_table)

print(f"Wrote {df.count()} rows to {target_table}")
```

If `openpyxl` is missing, add this cell at the top:

```python
%pip install openpyxl
dbutils.library.restartPython()
```

## Databricks Job

| Field | Value |
|---|---|
| Job ID | `432705911179775` |
| Job name | `bsc_finance_ingest` |
| Task name | `ingest` |
| Task type | Notebook |
| Source | Workspace |
| Path | `/Workspace/Shared/bsc_finance_ingest` |
| Compute | Serverless |
| **Owner** | _(assign a team member responsible for failures)_ |
| **Schedule** | Event-driven — triggered by Power Automate on file upload |
| **Source data** | `/Volumes/datahub_dev_bronze/scorecards_raw_files/finance/<file_name>` |
| **Target table** | `datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw` |
| **Downstream Tableau** | _(list any Tableau workbooks or data sources that read from the target table)_ |
| **Failure response** | Check Power Automate run history for the trigger step; verify file landed in the Volume; re-trigger manually from the job UI |

Do not define `file_name` as a job-level parameter with a blank default — this overrides the notebook widget's default with an empty string and causes the job to fail with `IsADirectoryError` on manual runs.

## Common Errors

### `403 Forbidden — required scopes: files`
PAT missing the `files` scope. Workspace admin must enable scoped tokens, then regenerate the PAT with the `files` scope added.

### `403 Forbidden — required scopes: jobs`
Same issue but for the `jobs` scope. Regenerate PAT with both scopes.

### File lands in Volume but shows 0.00 B
The HTTP Body is sending the JSON envelope instead of the decoded file content. Verify the Body expression is `base64ToBinary(body('Get_file_content_using_path')?['$content'])` entered via **fx** (not plain text).

### `IsADirectoryError: Is a directory: '/Volumes/.../finance/'`
The `file_name` parameter is empty. Either remove the blank job-level parameter or supply a default value.

### `DELTA_FAILED_TO_MERGE_FIELDS`
Schema mismatch with an existing Delta table. Add `.option("overwriteSchema", "true")` to the write call.

### `NotFound` on Get file content step
Using `Get file content` (by ID) with the `When a file is created (properties only)` trigger fails because the trigger outputs a list item ID, not a file ID. Use `Get file content using path` and pass the `Full path` dynamic value instead.
