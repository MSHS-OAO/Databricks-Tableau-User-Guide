# Compute - Notebooks and SQL

[Back to Table of Contents](../README.md#table-of-contents)

All code runs in Databricks on [compute](../Common%20Definitions.md). Team admins are responsible for creating [compute](../Common%20Definitions.md) and sharing it with the rest of the team. When a new workflow needs [compute](../Common%20Definitions.md), coordinate with the admins so the right option is available before work starts.

## Compute Types

We use two main compute types in this part of Databricks:

- **[All-purpose compute](../Common%20Definitions.md)**: Used for interactive [notebook](../Common%20Definitions.md) work, ad hoc analysis, and development.
- **[SQL warehouse](../Common%20Definitions.md)**: Used for SQL queries in the SQL editor, reporting, and dashboard work.

## Team Guidance

- Use serverless for all testing.
- Use serverless for production code when it is sufficient for the workload.
- Use job-specific [compute](../Common%20Definitions.md) for production notebook workflows when the code needs predictable configuration or isolation.
- Use a [SQL warehouse](../Common%20Definitions.md) in the SQL editor unless a different warehouse configuration is required.

## Notebooks

[Notebooks](../Common%20Definitions.md) are used for multi-language coding or work that goes beyond SQL alone.

1. Create or open the notebook in the [workspace](../Common%20Definitions.md).
2. Attach the right [compute](../Common%20Definitions.md) before running code.
3. Use [all-purpose compute](../Common%20Definitions.md) for exploration and development.
4. Use job-specific [compute](../Common%20Definitions.md) for scheduled production notebooks when needed.

## SQL Editor

The SQL editor is used when you only need SQL.

1. Open the SQL editor from Databricks or create a SQL file in the location where you want it to live.
2. Attach a [SQL warehouse](../Common%20Definitions.md) before writing or running queries.
3. Use serverless SQL for testing.
4. Use serverless SQL for production when it is sufficient for the query demand.

## Sharing Code

Anything you create in a personal [workspace](../Common%20Definitions.md) is only visible to you unless you share it. From a notebook or SQL file, use the share option in the top right corner to add individuals or all workspace users.

Sharing permissions:

1. **Can Manage**: User can edit, run, delete, share, and change compute access.
2. **Can Edit**: User can edit the code and run it.
3. **Can Run**: User can run the code but not change it.
4. **Can View**: User can only view the file.
