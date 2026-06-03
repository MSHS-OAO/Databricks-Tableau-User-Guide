# Job Scheduling

[Back to Table of Contents](../../README.md#table-of-contents)

A [Job](../../Common%20Definitions.md#job) that runs without an owner or documented schedule is a liability — when it fails at 2 AM, no one knows whose problem it is. These conventions ensure every scheduled pipeline is accountable and understood.

## Required Documentation for Every Production Job

Each guide file for a scheduled pipeline must include:

| Field | Description |
|---|---|
| **Owner** | The team member responsible for the job — who gets paged when it fails |
| **Schedule** | When it runs (e.g., daily at 6:00 AM ET, triggered by file upload) |
| **Source data** | What data the job reads (table, volume path, API, or external system) |
| **Target table** | Full Catalog path of the output table (e.g., `datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw`) |
| **Downstream Tableau** | Which Tableau workbook or data source consumes this table, if any |
| **Failure response** | What to do when the job fails (retry, notify someone, check the source) |

Use the template in each pipeline's guide file. See [SharePoint to Databricks](../../uploading-data/power-automate-sharepoint.md) for an example.

## Scheduling a Job in Databricks

1. Open the job in **Workflows → Jobs → [Job name]**
2. Click **Add trigger** → **Scheduled**
3. Choose **Quartz cron syntax** or the UI picker
4. Set the timezone to **America/New_York** (ET) for consistency
5. Click **Save**

Common cron expressions:

| Schedule | Cron |
|---|---|
| Daily at 6:00 AM ET | `0 0 6 * * ?` |
| Weekdays at 7:00 AM ET | `0 0 7 ? * MON-FRI` |
| Every 15 minutes | `0 0/15 * * * ?` |
| First of month at midnight | `0 0 0 1 * ?` |

## Avoiding Schedule Conflicts

Do not schedule a job to run at the same time that upstream data is expected to arrive. If the source file lands at 6:00 AM, schedule the ingest job for 6:15 AM or later — or use an event-driven trigger (like a Power Automate flow) so the job only runs when the file is actually present.

Build in tolerance for late data: if the job reads from an Oracle sync that sometimes runs 10 minutes late, add a 20-minute buffer.

## Identity: Service Principals over Personal PATs

For production jobs, prefer a service principal or approved automation identity over a personal [PAT](../../Common%20Definitions.md#personal-access-token-pat).

| Identity type | Use for |
|---|---|
| Personal PAT | Development and testing only |
| Service principal | Production jobs and Power Automate flows |

A personal PAT tied to a person's account will stop working if they leave or rotate their token. Service principals continue to work independently of individual accounts.

Contact your Databricks workspace admin to provision a service principal.

## Failure Notifications

Every production job should send an alert on failure. Configure this under **Job → Edit → Notifications → On failure**:

- Add the job owner's email
- Optionally add a team distribution list for critical pipelines

For jobs feeding Tableau dashboards, add the Tableau content owner to the notification list so they are aware of data delays.
