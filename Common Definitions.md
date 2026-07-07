# Common Definitions

[Back to Table of Contents](README.md#table-of-contents)

## Databricks Terms

- **All-purpose compute**: Interactive compute used for notebook development and ad hoc analysis.
- **Catalog**: The top-level Databricks container used to organize governed data.
- **Compute**: The Databricks environment that runs SQL, notebooks, and jobs. Teams choose shared, serverless, or job-specific compute based on the workload.
- **Git Folder**: A Databricks workspace folder connected to a Git repository.
- **Job**: A scheduled or manually triggered Databricks workflow that runs a task such as a notebook or query.
- **Notebook**: A Databricks document used to write and run code, SQL, notes, and analysis steps.
- **Schema**: A container inside a catalog that groups related tables and volumes.
- **SQL warehouse**: Compute used for SQL queries, dashboards, and reporting in the SQL editor.
- **Table**: A queryable dataset stored inside a schema.
- **Volume**: A governed file storage location inside a schema, often used for uploaded or staged files before they become tables.
- **Workspace**: The Databricks environment where users write notebooks, run jobs, manage compute, and access governed data.

## dbt Terms

- **dbt**: The SQL transformation framework our team uses after source data has landed in the Catalog.
- **dbt build**: A dbt command that runs models, tests, snapshots, and seeds for the selected project.
- **dbt model**: A SQL file in a dbt project that builds a view or table.
- **dbt source**: A named reference in dbt to an existing upstream table outside the dbt model flow.
- **Materialization**: The way dbt stores a model result, such as a view or table.
- **ref**: A dbt function used to reference another dbt model and manage build order.
- **source**: A dbt function used to reference an upstream source table defined in `schema.yml`.

## Tableau Terms

- **Datasource**: A reusable Tableau connection layer that defines where data comes from, how Tableau should query it, and the fields, calculations, and metadata available to workbooks.
- **Extract**: A Tableau-managed snapshot of data that is refreshed on a schedule and queried by Tableau instead of continuously querying the source system.
- **Live connection**: A Tableau connection type that queries the source system directly when users open or interact with a workbook.
