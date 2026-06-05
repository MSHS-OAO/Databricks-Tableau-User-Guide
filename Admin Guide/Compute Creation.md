# Compute Creation

[Back to Table of Contents](../README.md#table-of-contents)

This guide is for admins creating Databricks [compute](../Common%20Definitions.md#databricks-terms) for team use. The related user-facing guide is [Compute - Notebooks and SQL](../Databricks/Compute%20-%20Notebooks%20and%20SQL.md).

Team admins are responsible for creating shared [compute](../Common%20Definitions.md#databricks-terms), applying the right permissions, and confirming the [compute](../Common%20Definitions.md#databricks-terms) type matches the workflow. Use serverless options first for testing and for production workloads when serverless is sufficient. Use job-specific [compute](../Common%20Definitions.md#databricks-terms) for production [notebook](../Common%20Definitions.md#databricks-terms) workflows that need predictable configuration, isolation, or scheduled reliability.

## Before Creating Compute

Confirm these details before creating a new [SQL warehouse](../Common%20Definitions.md#databricks-terms) or [all-purpose compute](../Common%20Definitions.md#databricks-terms):

1. Whether the [compute](../Common%20Definitions.md#databricks-terms) supports testing, ad hoc analysis, scheduled production work, or Tableau reporting.
3. Which users or groups need access.
4. Whether the workload can use serverless [compute](../Common%20Definitions.md#databricks-terms).
5. Whether the workflow needs specific libraries, init scripts, secrets, or configuration.
6. Whether the workflow should use job-specific [compute](../Common%20Definitions.md#databricks-terms) instead of shared [all-purpose compute](../Common%20Definitions.md#databricks-terms).

Do not create personal all-purpose clusters for shared production [jobs](../Common%20Definitions.md#databricks-terms). Shared production workflows should use job-specific [compute](../Common%20Definitions.md#databricks-terms) when they need isolation or predictable dependency versions.

## SQL Warehouse

Use a [SQL warehouse](../Common%20Definitions.md#databricks-terms) for SQL Editor work, reporting, and dashboard queries. This is the expected [compute](../Common%20Definitions.md#databricks-terms) type for Tableau-facing datasets and routine SQL workflows unless a different warehouse configuration is required.

### Create a SQL Warehouse

1. In Databricks, open **SQL Warehouses** from the [compute](../Common%20Definitions.md#databricks-terms) area.
2. Select **Create SQL warehouse**.
4. Select a serverless warehouse option when this is sufficient.
5. Choose a size that matches the expected query demand.
6. Configure auto stop so the warehouse shuts down when it is idle.
7. Save the warehouse.
8. Grant access to the users or groups that need to run SQL or connect Tableau.

### Recommended Setup

Use this setup for most team [SQL warehouse](../Common%20Definitions.md#databricks-terms) requests:

| Setting | Recommendation |
| --- | --- |
| Cluster Size | X-Small or Small to start |
| Auto stop | Enabled so idle warehouses shut down |
| Compute type | Serverless [SQL warehouse](../Common%20Definitions.md#databricks-terms) when possible |
| Scaling | Set max at expected # of concurrent uses |
| Access | Grant access to the team users or groups that need SQL or Tableau connectivity |

## All-Purpose Compute

Use [all-purpose compute](../Common%20Definitions.md#databricks-terms) for interactive [notebook](../Common%20Definitions.md#databricks-terms) development, ad hoc analysis, and exploration. [All-purpose compute](../Common%20Definitions.md#databricks-terms) is not the default choice for shared production [jobs](../Common%20Definitions.md#databricks-terms).

### Create All-Purpose Compute

1. In Databricks, open **Compute**.
2. Select **Create compute**.
3. Set the policy as shared [compute](../Common%20Definitions.md#databricks-terms).
4. Set Databricks Runtime as the most recent LTS (long term support) version.
5. Choose a resource configuration appropriate for workload.
6. Configure auto termination so the [compute](../Common%20Definitions.md#databricks-terms) stops when idle.
7. Add any needed environment variables or init scripts.
8. Save the [compute](../Common%20Definitions.md#databricks-terms).
9. Grant access to the users or groups that will use the [compute](../Common%20Definitions.md#databricks-terms).

### When to Use All-Purpose Compute

Create or use [all-purpose compute](../Common%20Definitions.md#databricks-terms) when:

1. Serverless [compute](../Common%20Definitions.md#databricks-terms) is insufficient.
2. The work includes Python, SQL, or other [notebook](../Common%20Definitions.md#databricks-terms)-supported languages.
3. The team is exploring data before turning the work into a reusable workflow ([job](../Common%20Definitions.md#databricks-terms)).
4. A workflow is still in development and does not yet require job-specific [compute](../Common%20Definitions.md#databricks-terms).

For scheduled production [notebooks](../Common%20Definitions.md#databricks-terms), prefer job-specific [compute](../Common%20Definitions.md#databricks-terms) when the workflow needs stable dependencies, isolation, or reliability.

## Sharing and Permissions

After creating [compute](../Common%20Definitions.md#databricks-terms), share it with the correct users or groups. Use the least access that still lets the team do the work.

Common access levels:

1. **Can Manage**: User can change [compute](../Common%20Definitions.md#databricks-terms) configuration and permissions.
2. **Can Attach To**: User can attach [notebooks](../Common%20Definitions.md#databricks-terms) or workloads to the [compute](../Common%20Definitions.md#databricks-terms).
3. **Can Restart**: User can restart the [compute](../Common%20Definitions.md#databricks-terms) when needed.
