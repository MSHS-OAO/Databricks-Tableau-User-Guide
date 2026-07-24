# Job Scheduling

[Back to Table of Contents](../README.md#table-of-contents)

Creating a [job](../Common%20Definitions.md#databricks-terms) is the final step in the process of creating an ETL and is only done after the individual [notebooks](../Common%20Definitions.md#databricks-terms) and [dbt models](../Common%20Definitions.md#dbt-terms) have been developed. See [Notebooks](../Databricks/Compute%20-%20Notebooks%20and%20SQL.md) and [DBT](../Admin%20Guide/Databricks/DBT.md) for reference.

<u>**Team Guidelines**</u>: All projects should rely on a staging and production ETL [job](../Common%20Definitions.md#databricks-terms). The staging job will populate data in the staging [schema](../Common%20Definitions.md#databricks-terms) and production job will populate data in the production [schema](../Common%20Definitions.md#databricks-terms). To clarify, these will use the standard Job scheduling, not the ETL pipeline. In unique circumstances, ad hoc [jobs](../Common%20Definitions.md#databricks-terms) will be scheduled for automated reporting, and in this case reach out to admins for guidance.

## Workflow

All ETL [jobs](../Common%20Definitions.md#databricks-terms) should follow this workflow pattern:
1. Schedule all [notebooks](../Common%20Definitions.md#databricks-terms) responsible for bringing external data into Databricks.
   1. Note that the need for this step should decrease as DTP brings more data into our Databricks environment.
2. Schedule a dbt task that creates all [tables](../Common%20Definitions.md#databricks-terms)/views and runs all necessary column tests.

## Creating an ETL Job
For example ETL [jobs](../Common%20Definitions.md#databricks-terms), please reference [Oncology Data Pull - Staging](https://adb-7405606624435497.17.azuredatabricks.net/jobs/159438108881197/tasks?o=7405606624435497) or [Oncology Data Pull - Production](https://adb-7405606624435497.17.azuredatabricks.net/jobs/1123277539237064/tasks?o=7405606624435497) for staging and production examples respectively.

1. Determine if this is a staging, production, or ad hoc [job](../Common%20Definitions.md#databricks-terms).
2. Navigate to the Jobs & Pipelines section and select create job.
   
<img src="../images/create job.PNG" width="1000">

4. If the ETL requires pulling in data from an external source, then schedule the necessary notebook(s).
    1. Name the task as desired
    2. Select notebook task type.
    3. Use GitHub repo as source and select staging/main as needed based on step 1.
    4. Select path to notebook.
    5. Select `OAO_PRODUCTION_JOB_COMPUTE` for [compute](../Common%20Definitions.md#databricks-terms) option.
    6. There should be no dependencies since this should be your first step.
    7. Add any notebook parameters if needed.
5. Add dbt task.
    1. Name the task as desired
    2. Select dbt task type.
    3. Use GitHub repo as source and select staging/main as needed based on step 1.
    4. Input folder with dbt files.
    5. Add dbt commands of `dbt deps` and [dbt build](../Common%20Definitions.md#dbt-terms) in that order.
    6. Select Serverless Starter Warehouse.
    7. Select `opsanalytics_adb_workspace01` as [Catalog](../Common%20Definitions.md#databricks-terms).
    8. Select appropriate staging/production [schema](../Common%20Definitions.md#databricks-terms) based on [Architecture](../Databricks/Architecture.md) guidelines and the decision at step 1.
    9. Select Serverless dbt CLI compute.
    10. Set dependencies to any notebook(s) scheduled in step 4.
    11. Run if dependencies all succeeded
    12. Set `dbt-default` as Environment and Libraries.
6. Now that tasks have been scheduled, set job settings in the right-hand pane of task view.
    1. Set schedule and trigger to either Scheduled, File arrival, or Table update as needed for workflow.
    2. Set up job notifications to trigger a message in the appropriate Teams channel on success and on failure.
        1. Refer to [Job Notifications](../Admin%20Guide/Job%20Notifications.md) for more details.
    3. Ensure Git repo and proper branch are configured.
    4. Ensure the job-specific dbt [service principal](../Common%20Definitions.md#databricks-terms) is given `Can Manage Run` permissions.
