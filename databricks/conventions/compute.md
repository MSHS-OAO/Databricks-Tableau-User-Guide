# Knowing What Compute to Use

[Back to Table of Contents](../../README.md#table-of-contents)

Compute is the processing power that runs your notebooks, SQL queries, and jobs. Choosing the wrong compute type wastes money or causes reliability problems. This page explains the options and when to use each.

> This guidance reflects our team's current patterns. Expect it to evolve. For the most current details, see `Databricks/Compute - Notebooks and SQL.md`.

## Compute Types

| Type | Best for | Startup time | Idle cost |
|---|---|---|---|
| [Serverless Compute](../../Common%20Definitions.md#serverless-compute) | Notebooks, ad-hoc SQL, scheduled jobs | Seconds | None |
| SQL Warehouse | SQL Editor queries, Tableau Live connections | Seconds (serverless) to 2 min (classic) | None when stopped |
| Job Cluster | Production jobs with fixed library versions | 3–5 min | None (terminates after run) |
| All-purpose Cluster | Interactive development with custom config | 3–5 min | Accrues cost while running |

## Rules

### Use Serverless for most work
Serverless compute covers the majority of our use cases:
- Routine SQL exploration in notebooks
- Lightweight data transformations
- Scheduled ingestion jobs (Power Automate → Databricks pipelines)
- One-off data pulls

Serverless starts in seconds and costs nothing when idle. Use it as the default until there is a specific reason not to.

### Use a Job Cluster for production workflows that need fixed dependencies
If a job depends on a specific library version — such as a pinned version of `pandas`, `oracledb`, or a custom wheel — use a job-specific cluster with the library attached. This prevents a Databricks platform update from silently breaking the job.

Configure the cluster in the job's **Compute** tab → **Create new job cluster** → attach libraries under the **Libraries** tab.

### Use a SQL Warehouse for the SQL Editor and Tableau
The SQL Editor and Tableau's Live connection mode both require a SQL Warehouse, not a notebook cluster. Use the shared serverless SQL Warehouse where available. Stop it when not in use.

### Avoid personal all-purpose clusters for shared jobs
Do not run team jobs on a personal all-purpose cluster. If the cluster is stopped or deleted, the job fails. Always attach shared jobs to a job cluster or serverless compute.

## Documenting Compute in Workflow Guides
Every workflow guide in this repository should state the expected compute type near the top — before the setup steps — so a user knows what to start before running code.

Example:

> **Compute**: Serverless. No cluster setup required.

or

> **Compute**: Job cluster with Oracle JDBC JAR attached as a library. See [Compute Creation](../../admin-guide/compute-creation.md) for setup steps.
