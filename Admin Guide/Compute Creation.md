# Compute Creation

[Back to Table of Contents](../README.md#table-of-contents)

This guide is for admins creating Databricks [compute](../Common%20Definitions.md#databricks-terms) for team use. The related user-facing guide is [Compute - Notebooks and SQL](../Databricks/Compute%20-%20Notebooks%20and%20SQL.md).

Team admins are responsible for creating shared compute, applying the right permissions, and confirming the compute type matches the workflow. Use serverless options first for testing and for production workloads when serverless is sufficient. Use job-specific compute for production notebook workflows that need predictable configuration, isolation, or scheduled reliability.

## Before Creating Compute

Confirm these details before creating a new SQL warehouse or all-purpose compute:

1. Who owns the workflow or dashboard.
2. Whether the compute supports testing, ad hoc analysis, scheduled production work, or Tableau reporting.
3. Which users or groups need access.
4. Whether the workload can use serverless compute.
5. Whether the workflow needs specific libraries, init scripts, secrets, or configuration.
6. Whether the workflow should use job-specific compute instead of shared all-purpose compute.

Do not create personal all-purpose clusters for shared production jobs. Shared production workflows should use job-specific compute when they need isolation or predictable dependency versions.

## SQL Warehouse

Use a [SQL warehouse](../Common%20Definitions.md#databricks-terms) for SQL editor work, reporting, and dashboard queries. This is the expected compute type for Tableau-facing datasets and routine SQL workflows unless a different warehouse configuration is required.

### Create a SQL Warehouse

1. In Databricks, open **SQL Warehouses** from the compute area.
2. Select **Create SQL warehouse**.
3. Choose a clear lowercase name with underscores.
4. Select a serverless warehouse option when available.
5. Choose a size that matches the expected query demand.
6. Configure auto stop so the warehouse shuts down when it is idle.
7. Save the warehouse.
8. Grant access to the users or groups that need to run SQL or connect Tableau.

### Recommended Setup

Use this setup for most team SQL warehouse requests:

| Setting | Recommendation |
| --- | --- |
| Compute type | Serverless SQL warehouse when available |
| Naming | Lowercase with underscores |
| Access | Grant access to the team users or groups that need SQL or Tableau connectivity |
| Auto stop | Enabled so idle warehouses shut down |
| Production use | Allowed when serverless is sufficient for the workload |

Example names:

```text
hso_reporting_sql
hso_tableau_sql
project_name_sql
```

### When to Use a SQL Warehouse

Create or use a SQL warehouse when:

1. Users are writing SQL in the SQL editor.
2. Tableau needs to connect to Databricks.
3. A dashboard or published datasource needs routine query access.
4. The work does not require notebook-specific libraries or multi-language code.

## All-Purpose Compute

Use [all-purpose compute](../Common%20Definitions.md#databricks-terms) for interactive notebook development, ad hoc analysis, and exploration. All-purpose compute is not the default choice for shared production jobs.

### Create All-Purpose Compute

1. In Databricks, open **Compute**.
2. Select **Create compute**.
3. Choose a clear lowercase name with underscores.
4. Select a serverless option when available and appropriate.
5. Choose a runtime and configuration that match the development workload.
6. Configure auto termination so the compute stops when idle.
7. Add only the libraries or configuration needed for the workflow.
8. Save the compute.
9. Grant access to the users or groups that need to attach notebooks.

### Recommended Setup

Use this setup for most team all-purpose compute requests:

| Setting | Recommendation |
| --- | --- |
| Compute type | Serverless when available and sufficient |
| Naming | Lowercase with underscores |
| Access | Grant only to the users or groups doing notebook work |
| Auto termination | Enabled so idle compute shuts down |
| Production use | Avoid for shared production jobs unless there is a specific approved reason |

Example names:

```text
hso_dev_all_purpose
project_name_dev
team_analysis_compute
```

### When to Use All-Purpose Compute

Create or use all-purpose compute when:

1. Users need to run Databricks notebooks interactively.
2. The work includes Python, SQL, or other notebook-supported languages.
3. The team is exploring data before turning the work into a reusable workflow.
4. A workflow is still in development and does not yet require job-specific compute.

For scheduled production notebooks, prefer job-specific compute when the workflow needs stable dependencies, isolation, or reliability.

## Sharing and Permissions

After creating compute, share it with the correct users or groups. Use the least access that still lets the team do the work.

Common access levels:

1. **Can Manage**: User can change compute configuration and permissions.
2. **Can Attach To**: User can attach notebooks or workloads to the compute.
3. **Can Restart**: User can restart the compute when needed.

Give admin-level access only to users responsible for maintaining the compute. Most users should only receive the access needed to run notebooks, SQL, or Tableau connections.

## Documentation Expectations

For each shared compute resource, document:

1. Compute name.
2. Compute type, such as SQL warehouse or all-purpose compute.
3. Owner.
4. Intended use.
5. Users or groups with access.
6. Whether the compute is approved for production use.
7. Any special libraries, secrets, or configuration.

If the compute supports a Tableau datasource or dashboard, include the SQL warehouse name in the related Tableau guide or publishing notes.
