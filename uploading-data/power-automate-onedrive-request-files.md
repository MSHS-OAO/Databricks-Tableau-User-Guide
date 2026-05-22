# Power Automate — OneDrive Request Files to Databricks

The **Request Files** feature in OneDrive lets you create a link that anyone — even people outside your organization — can use to upload files to a specific OneDrive folder. Power Automate can watch that folder and automatically push new files to Databricks.

## Architecture

```
OneDrive "Request Files" link shared with external user
        ↓ (external user uploads file via link)
OneDrive for Business folder
        ↓ (file appears in watched folder)
Power Automate Flow
        ↓
   1. When a file is created — OneDrive trigger
   2. Get file content — fetches file bytes
   3. HTTP PUT → Databricks Files API — uploads to Volume
   4. HTTP POST → Databricks Jobs API — triggers ingest job
        ↓
Databricks Job (notebook)
        ↓
Delta Table in Unity Catalog
```

## Prerequisites

- Microsoft 365 account with OneDrive for Business
- Power Automate access
- Databricks workspace with Unity Catalog enabled
- Personal Access Token with `files` and `jobs` scopes

## Step 1: Create the Request Files Link

1. Open **OneDrive for Business** in a browser
2. Navigate to the folder where uploaded files should land (create one if needed, e.g., `DataFeeds/Submissions`)
3. Right-click the folder → **Request files**
4. Enter a description (e.g., "Upload your monthly report here")
5. Click **Copy link** and share it with submitters

Files uploaded through this link appear directly in the `DataFeeds/Submissions` folder.

## Step 2: Power Automate Flow

### Action 1: When a file is created (OneDrive for Business)

| Field | Value |
|---|---|
| Folder | `/DataFeeds/Submissions` (or your chosen folder) |

This trigger fires every time a new file appears in the folder, including files uploaded via the Request Files link.

### Action 2: Get file content

| Field | Value |
|---|---|
| File | `Id` (dynamic content from trigger) |

Unlike SharePoint, the OneDrive trigger provides a file ID directly compatible with the **Get file content** action (not the `using path` variant).

### Action 3: HTTP PUT — Upload to Volume

| Field | Value |
|---|---|
| Method | `PUT` |
| URI | `https://<workspace>.azuredatabricks.net/api/2.0/fs/files/Volumes/<catalog>/<schema>/<volume>/@{triggerOutputs()?['body/Name']}` |
| Header: Authorization | `Bearer <PAT>` |
| Header: Content-Type | `application/octet-stream` |
| Body (expression) | `base64ToBinary(body('Get_file_content')?['$content'])` |

Enter the Body expression via the **fx** button.

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
    "file_name": "@{triggerOutputs()?['body/Name']}"
  }
}
```

## Step 3: Databricks Notebook

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

## Sending Confirmation to the Submitter

OneDrive's Request Files feature does not automatically notify the submitter that their file was received. Add an **Outlook — Send an email (V2)** action at the end of the flow:

| Field | Value |
|---|---|
| To | Can only notify a fixed address (external uploader's email is not captured by the trigger) |
| Subject | `File received: @{triggerOutputs()?['body/Name']}` |
| Body | File has been uploaded and is being processed. |

For a proper confirmation loop with external parties, consider a **Microsoft Forms** → OneDrive approach instead, which captures the submitter's email.

## Limitations of Request Files

- The uploader's identity is not exposed to the Power Automate trigger — you only get the filename
- Files uploaded via Request Files overwrite existing files with the same name
- Folder-level Request Files links cannot be scoped to subfolders

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| Trigger does not fire | Flow is off, or watched folder path is wrong | Verify folder path and enable the flow |
| `403 Forbidden — required scopes: files` | PAT missing `files` scope | Regenerate PAT |
| File arrives as 0 bytes | Body expression not evaluated via fx | Re-enter expression using fx button |
| `IsADirectoryError` in notebook | `file_name` dynamic content resolves to empty | Check `triggerOutputs()?['body/Name']` in test output |
