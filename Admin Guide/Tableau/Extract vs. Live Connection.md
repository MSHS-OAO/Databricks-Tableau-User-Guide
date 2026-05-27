# Extract vs. Live Connection

[Back to Table of Contents](../../README.md#table-of-contents)

## What This Choice Controls

When publishing a Tableau [Datasource](../../Common%20Definitions.md#tableau-terms), choose whether Tableau should use a [live connection](../../Common%20Definitions.md#tableau-terms) or an [extract](../../Common%20Definitions.md#tableau-terms).

A live connection sends queries from Tableau to the source system when someone opens or interacts with a workbook. An extract copies a snapshot of the data into Tableau so Tableau can query its own optimized copy.

For the majority of our work we will use a Databricks connector with an extract datasoruce. The reason is most of our data will live in Databricks and an extract, while a little slower to create, will result in quicker dashboards and lower costs on the Databricks environment. We will use live connections sparingly when using a one drive connector. This will be our connection method if we need external inputs of data. 

## Live Connections

A live connection keeps Tableau connected directly to the source data. When a user filters a view, opens a dashboard, or refreshes a sheet, Tableau sends queries back to the source system.

Use a live connection when:

1. The dashboard needs the most current data available.
2. The source table is in Databricks and is designed for reporting or dashboard use.
3. The dashboard is backed by a table that performs well with interactive filters and aggregations.
4. The source data refreshes often enough that a scheduled extract would become stale too quickly.

Avoid a live connection when:

1. The source query is slow, complex, or depends on many joins.
2. Many Tableau users will interact with the dashboard at the same time and could add load to the source system.
3. The dashboard only needs a daily, weekly, or monthly snapshot.

## Extracts

An extract stores a Tableau-managed copy of the data. Tableau queries the extract instead of continuously querying the original source. Extracts can be refreshed on a schedule so the published datasource stays current enough for the dashboard's business need. Extracts are optimized for tableau, so an extract will always outperform the same datasource as a live connection. Alwasy use extracts when it fits the use case.

Use an extract when:

1. Dashboard speed is more important than seeing every source-system change immediately.
2. The data only needs to refresh on a predictable schedule, such as daily or weekly.
3. The source is Oracle and repeated live dashboard queries could create unnecessary load.
4. The dashboard needs a stable reporting snapshot for a specific refresh cycle.

Avoid an extract when:

1. Users must see data changes as soon as they are available in the source.
2. The refresh schedule cannot be aligned with upstream file delivery or database refresh timing.

## Refresh and Ownership Expectations

For published extracts, document the refresh schedule and owner before the datasource is treated as production-ready. The datasource owner is responsible for confirming that the extract refresh timing does not overlap with upstream file delivery, Oracle refresh windows, or Databricks job schedules.

For datasources that feed business operations, include these details in the related guide or publishing notes:

1. Source system, such as Databricks, Oracle, or OneDrive/SharePoint.
2. Full source location, such as Catalog, schema, and table for Databricks.
3. Whether the datasource is live or extract.
4. Extract refresh schedule, if applicable.
5. Dashboard owner and expected failure response path.
