# Power Automate — Outlook to Databricks

This pipeline watches an Outlook mailbox for emails with file attachments and automatically uploads those attachments to a Databricks Catalog [Volume](../Common%20Definitions.md#volume), then triggers a [Job](../Common%20Definitions.md#job) to ingest them.

## Architecture

```
Outlook Inbox
        ↓ (email with attachment arrives)
Power Automate Flow
        ↓ (4 actions)
   1. When a new email arrives (V3) — Outlook trigger
   2. Get attachment (loop) — fetches attachment bytes
   3. HTTP PUT → Databricks Files API — uploads to Volume
   4. HTTP POST → Databricks Jobs API — triggers ingest job
        ↓
Databricks Job (notebook)
        ↓
Delta Table in Catalog
```

## Prerequisites

- Microsoft 365 account with an Outlook mailbox and [Power Automate](../Common%20Definitions.md#power-automate) access
- Databricks workspace with Catalog enabled
- [Personal Access Token](../Common%20Definitions.md#personal-access-token-pat) with `files` and `jobs` scopes
- Target [Volume](../Common%20Definitions.md#volume) already created in the Catalog

## Power Automate Flow

### Action 1: When a new email arrives (V3)

| Field | Value |
|---|---|
| Folder | `Inbox` (or a specific sub-folder) |
| Include Attachments | **Yes** |
| Only with Attachments | **Yes** |

Optionally filter by subject line using **Show advanced options → Subject filter**:

```
Subject filter: [DATA FEED]
```

This limits the trigger to emails whose subject contains `[DATA FEED]`, reducing noise.

### Action 2: Apply to each — loop over attachments

Outlook emails can have multiple attachments. Use an **Apply to each** loop:

- **Select an output from previous steps**: `Attachments` (dynamic content from trigger)

Inside the loop, add the upload and job-trigger actions so each attachment is processed.

### Action 3: HTTP PUT — Upload to Volume

| Field | Value |
|---|---|
| Method | `PUT` |
| URI | `https://<workspace>.azuredatabricks.net/api/2.0/fs/files/Volumes/<catalog>/<schema>/<volume>/@{items('Apply_to_each')?['Name']}` |
| Header: Authorization | `Bearer <PAT>` |
| Header: Content-Type | `application/octet-stream` |
| Body (expression) | `base64ToBinary(items('Apply_to_each')?['ContentBytes'])` |

The `ContentBytes` field on an Outlook attachment is already base64-encoded. The expression decodes it to raw binary before sending to the Databricks Files API.

Enter the expression via the **fx** button — not as plain text.

### Action 4: HTTP POST — Trigger Databricks Job

| Field | Value |
|---|---|
| Method | `POST` |
| URI | `https://<workspace>.azuredatabricks.net/api/2.1/jobs/run-now` |
| Header: Authorization | `Bearer <PAT>` |
| Header: Content-Type | `application/json` |
| Body | See below |

```json
{
  "job_id": <job_id>,
  "job_parameters": {
    "file_name": "@{items('Apply_to_each')?['Name']}"
  }
}
```

## Databricks Notebook

```python
dbutils.widgets.text("file_name", "default.xlsx")
file_name = dbutils.widgets.get("file_name")

volume_path = f"/Volumes/<catalog>/<schema>/<volume>/{file_name}"
target_table = "<catalog>.<schema>.<table>"

import pandas as pd
pdf = pd.read_excel(volume_path)
df = spark.createDataFrame(pdf)

df.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable(target_table)
print(f"Wrote {df.count()} rows to {target_table}")
```

## Filtering by Sender

To only process emails from a trusted sender, add a **Condition** action after the trigger:

- **Condition**: `From` is equal to `trusted-sender@example.com`
- **If yes**: continue with upload and job trigger
- **If no**: do nothing (leave the No branch empty)

## Handling Multiple File Types

Use a **Switch** action on `items('Apply_to_each')?['Name']` extension to route different file types to different notebooks:

```
Switch on: @{last(split(items('Apply_to_each')?['Name'], '.'))}
Case '.xlsx': trigger job_id for Excel ingestion
Case '.csv':  trigger job_id for CSV ingestion
```

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| `403 Forbidden — required scopes: files` | PAT missing `files` scope | Regenerate PAT with `files` scope |
| File arrives as 0 bytes | `ContentBytes` not decoded via `base64ToBinary` | Enter expression via fx button |
| Loop processes 0 attachments | `Include Attachments` not set to Yes on trigger | Edit trigger settings |
| `IsADirectoryError` in notebook | `file_name` parameter is empty | Ensure `Name` dynamic content resolves correctly |
