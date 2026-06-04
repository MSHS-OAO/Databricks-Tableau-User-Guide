# What is a Job?

A **Databricks Job** schedules and runs tasks automatically — without anyone opening a [Notebook](../Common%20Definitions.md#notebook) and clicking Run. Jobs are the production mechanism: once data pipelines are tested interactively, they get promoted into a job so they run on a schedule or on demand.

## Job vs Notebook

| | Notebook | Job |
|---|---|---|
| Who triggers it | A person, manually | A schedule or an API call |
| Compute lifecycle | Uses whatever cluster the notebook is attached to | Spins up its own cluster, runs, terminates |
| Parameterization | Widgets set by hand | `job_parameters` passed via API |
| Logging | Cell output | Structured run history with status and duration |

## Creating a Job

1. In the Databricks sidebar, go to **Workflows → Jobs**
2. Click **Create job**
3. Configure the task:

| Field | Description |
|---|---|
| Task name | Short identifier, no spaces (e.g. `ingest`) |
| Task type | Usually `Notebook` |
| Source | `Workspace` for notebooks stored in `/Workspace/...` |
| Path | Full workspace path to the notebook |
| Compute | `Serverless` (fastest startup) or a specific cluster |

4. Optionally set a **Schedule** (cron expression or UI picker)
5. Click **Create**

## Running a Job

**Manually**: Open the job, click **Run now**.

**Via API (Power Automate or any HTTP client)**:

```http
POST https://<workspace>.azuredatabricks.net/api/2.1/jobs/run-now
Authorization: Bearer <PAT>
Content-Type: application/json

{
  "job_id": 432705911179775,
  "job_parameters": {
    "file_name": "report.xlsx"
  }
}
```

The response contains a `run_id`. Use it to poll the run status:

```http
GET https://<workspace>.azuredatabricks.net/api/2.1/jobs/runs/get?run_id=<run_id>
Authorization: Bearer <PAT>
```

## Job Parameters

Job parameters override notebook widget defaults at runtime. Declare a widget in the notebook:

```python
dbutils.widgets.text("file_name", "default.xlsx")
file_name = dbutils.widgets.get("file_name")
```

Pass the override via the API:

```json
{
  "job_parameters": {
    "file_name": "actual_file.xlsx"
  }
}
```

**Gotcha**: If you also define `file_name` as a job-level parameter with a blank default value, it overrides the notebook widget's default on manual runs. This causes `IsADirectoryError` because the file path resolves to a directory. Either leave the job-level parameter out entirely, or give it a valid default.

## Viewing Run History

Each run logs:
- Start time, end time, duration
- Status: `SUCCESS`, `FAILED`, `RUNNING`, `CANCELED`
- Full output from each cell

To view: **Workflows → Jobs → [Job name] → Runs tab**

Click any run to see the notebook output as it was at execution time.

## Email Notifications

Configure email alerts on job failure:

1. Open the job
2. Click **Edit** → **More options → Notifications**
3. Add email addresses for **On failure** and optionally **On success**

## Compute Recommendation

Use [Serverless Compute](../Common%20Definitions.md#serverless-compute) for jobs that run infrequently or need fast startup. Serverless clusters start in under 30 seconds and cost nothing when idle.

Use a **dedicated cluster** only if the job needs specific libraries or configurations not available on serverless. See [Knowing What Compute to Use](../Databricks/conventions/compute.md) for the full decision guide.
