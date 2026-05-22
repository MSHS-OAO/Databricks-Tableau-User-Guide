# Job Scheduling

[Back to Table of Contents](../README.md#table-of-contents)

[Jobs](../Common%20Definitions.md) should be documented with the expected [compute](../Common%20Definitions.md), source query, target output, and owner before they are scheduled.

## Workflow 1: Schedule a Simple SQL Query

Use this pattern when the work is a single SQL statement that writes directly to a table or refreshes a reporting dataset.

1. Create or open the SQL query in Databricks.
2. Verify the query returns the expected result and references the full `catalog.schema.table` name where needed.
3. Save the query in the shared [workspace](../Common%20Definitions.md) or [Git folder](../Common%20Definitions.md).
4. Create a [Job](../Common%20Definitions.md) from the SQL query.
5. Set the schedule, owner, and alerting path.
6. Run the [job](../Common%20Definitions.md) once manually before turning on the schedule.

Example use case:

```text
Refresh a reporting table each morning from a single SQL query.
```

## Workflow 2: Schedule a SQL Query That Feeds a Notebook

Use this pattern when the SQL output is an input step for a [notebook](../Common%20Definitions.md) that performs additional transformation, validation, or file generation.

1. Write and validate the SQL query that produces the source dataset.
2. Save the SQL output to a table or view that the notebook can read reliably.
3. Build the [notebook](../Common%20Definitions.md) step to read from that table or view and complete the downstream work.
4. Create a multi-task [Job](../Common%20Definitions.md) or a [Job](../Common%20Definitions.md) with dependent tasks.
5. Put the SQL task before the notebook task so the notebook always sees fresh data.
6. Test both tasks together before scheduling.

Use this pattern when:

- The SQL step prepares or filters the data.
- The notebook applies business logic, writes files, or performs checks.
- The workflow needs a clear handoff between SQL and notebook code.

## Scheduling Rules

- Use the smallest workflow that meets the need.
- Give the [job](../Common%20Definitions.md) a clear owner and a failure response path.
- Avoid schedules that overlap with upstream file delivery or known refresh windows unless the workflow handles late data.
- Document the job in the related guide page when it supports Tableau or another shared dependency.
