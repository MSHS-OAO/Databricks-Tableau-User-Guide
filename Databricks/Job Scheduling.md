# Job Scheduling

[Back to Table of Contents](../README.md#table-of-contents)

Creating a job is the final step in the process of creating an ETL and is only done after the individual notebooks and DBT models have been developed. See [Notebooks](../Databricks/Compute%20-%20Notebooks%20and%20SQL.md) and [DBT](/Admin%20Guide/DBT.md) for reference.

<u>**Team Guidelines**</u>: All projects should rely on a single ETL job responsible for all data transformations. To clarify, these will use the standard Job scheduling not the ETL pipeline. In unique circumstances adhoc jobs will be scheduled for automated reporting and in this case reach out to admins for guidance.

## Workflow

All ETL jobs should follow this workflow pattern:
1. Schedule all notebooks responsible for bringing external data into databricks. 
   1. Note that the need for this step should decrease DTP brings more data into our databricks environment
2. Schedule a DBT task that creates all tables/views and runs all necessary column tests

## Creating an ETL Job
For example ETL jobs please reference [Oncology Data Pull - Staging](https://adb-7405606624435497.17.azuredatabricks.net/jobs/159438108881197/tasks?o=7405606624435497) or [Oncology Data Pull - Production](https://adb-7405606624435497.17.azuredatabricks.net/jobs/1123277539237064/tasks?o=7405606624435497) for staging and production examples respectively.

1. Determine if this is a staging, production or adhoc job
2. Navigate to the Jobs & Pipelines section and select create job
<img src="../images/create job.PNG" width="1000">
3. If the ETL requires pulling in data from an external source then schedule the necessary notebook(s)
    1. Name the task as desired
    2. Select notebook task type
    3. Use github repo as source and select staging/main as needed based on step 1
    4. Select path to notebook
    5. select OAO_PRODUCTION_JOB_COMPUTE for compute option
    6. There should be no dependencies since this should be your first step
    7. add any notebook parameters if needed
4. Add DBT task
    1. Name the task as desired
    2. Select dbt task type
    3. Use github repo as source and select staging/main as needed based on step 1
    4. Input folder with dbt files
    5. add dbt commands of `dbt deps` and `dbt build` in that order
    6. select Serverless Starter Warehouse
    7. select opsanalytics_adb_workspace01 as catalog
    8. select appropriate staging/production schema based on [Architecture](../Databricks/Architecture.md) guidelines and the decision at step 1
    9. select Serverless dbt CLI compute
    10. set dependencies to any notebook(s) scheduled in step 3
    11. Run if dependencies all succeeded
    12. set dbt-default as Environment and Libraries
5. Now that tasks have been scheduled, set job settings in right hand pane of task view
    1. Set schedule and trigger to either Scheduled, File arrival or Table update as needed for workflow
    2. Set job parameter `trigger_source` = `{{job.trigger.type}}`
    3. Set up job notifiactions to trigger message in appropriate teams channel on success and on failure
        1. refer to [Job Notifications](/Admin%20Guide/Job%20Notifications.md) for more details.
    4. Ensure git repo and proper branch are configured
    5. Ensure the job specific dbt service principal is given `Can Manage Run` permissions