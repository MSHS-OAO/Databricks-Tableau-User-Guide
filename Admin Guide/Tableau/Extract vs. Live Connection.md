# Extract vs. Live Connection

[Back to Table of Contents](../../README.md#table-of-contents)

## What This Choice Controls

When publishing a Tableau [Datasource](../../Common%20Definitions.md#tableau-terms), choose whether Tableau should use a [live connection](../../Common%20Definitions.md#tableau-terms) or an [extract](../../Common%20Definitions.md#tableau-terms).

A [live connection](../../Common%20Definitions.md#tableau-terms) sends queries from Tableau to the source system when someone opens or interacts with a workbook. An [extract](../../Common%20Definitions.md#tableau-terms) copies a snapshot of the data into Tableau so Tableau can query its own optimized copy.

For the majority of our work, we will use a Databricks connector with an [extract](../../Common%20Definitions.md#tableau-terms) [datasource](../../Common%20Definitions.md#tableau-terms). The reason is most of our data will live in Databricks, and an [extract](../../Common%20Definitions.md#tableau-terms), while a little slower to create, will result in quicker dashboards and lower costs on the Databricks environment. We will use [live connections](../../Common%20Definitions.md#tableau-terms) sparingly when using a OneDrive connector. This will be our connection method if we need external inputs of data.

## Live Connections

A [live connection](../../Common%20Definitions.md#tableau-terms) keeps Tableau connected directly to the source data. When a user filters a view, opens a dashboard, or refreshes a sheet, Tableau sends queries back to the source system.

Use a [live connection](../../Common%20Definitions.md#tableau-terms) when:

1. The dashboard needs the most current data available.
2. The source [table](../../Common%20Definitions.md#databricks-terms) is in Databricks and is designed for reporting or dashboard use.
3. The dashboard is backed by a [table](../../Common%20Definitions.md#databricks-terms) that performs well with interactive filters and aggregations.
4. The source data refreshes often enough that a scheduled [extract](../../Common%20Definitions.md#tableau-terms) would become stale too quickly.

Avoid a [live connection](../../Common%20Definitions.md#tableau-terms) when:

1. The source query is slow, complex, or depends on many joins.
2. Many Tableau users will interact with the dashboard at the same time and could add load to the source system.
3. The dashboard only needs a daily, weekly, or monthly snapshot.

## Extracts

An [extract](../../Common%20Definitions.md#tableau-terms) stores a Tableau-managed copy of the data. Tableau queries the [extract](../../Common%20Definitions.md#tableau-terms) instead of continuously querying the original source. Extracts can be refreshed on a schedule so the published [datasource](../../Common%20Definitions.md#tableau-terms) stays current enough for the dashboard's business need. Extracts are optimized for Tableau, so an [extract](../../Common%20Definitions.md#tableau-terms) will always outperform the same [datasource](../../Common%20Definitions.md#tableau-terms) as a [live connection](../../Common%20Definitions.md#tableau-terms). Always use extracts when they fit the use case.

Use an [extract](../../Common%20Definitions.md#tableau-terms) when:

1. Dashboard speed is more important than seeing every source-system change immediately.
2. The data only needs to refresh on a predictable schedule, such as daily or weekly.
3. The source is Oracle and repeated live dashboard queries could create unnecessary load.
4. The dashboard needs a stable reporting snapshot for a specific refresh cycle.

Avoid an [extract](../../Common%20Definitions.md#tableau-terms) when:

1. Users must see data changes as soon as they are available in the source.
2. The refresh schedule cannot be aligned with upstream file delivery or database refresh timing.

## Refresh and Ownership Expectations

For published extracts, document the refresh schedule and owner before the [datasource](../../Common%20Definitions.md#tableau-terms) is treated as production-ready. The [datasource](../../Common%20Definitions.md#tableau-terms) owner is responsible for confirming that the [extract](../../Common%20Definitions.md#tableau-terms) refresh timing does not overlap with upstream file delivery, Oracle refresh windows, or Databricks [job](../../Common%20Definitions.md#databricks-terms) schedules.

For datasources that feed business operations, include these details in the related guide or publishing notes:

1. Source system, such as Databricks, Oracle, or OneDrive/SharePoint.
2. Full source location, such as [Catalog](../../Common%20Definitions.md#databricks-terms), [schema](../../Common%20Definitions.md#databricks-terms), and [table](../../Common%20Definitions.md#databricks-terms) for Databricks.
3. Whether the [datasource](../../Common%20Definitions.md#tableau-terms) is live or an [extract](../../Common%20Definitions.md#tableau-terms).
4. Extract refresh schedule, if applicable.
5. Dashboard owner and expected failure response path.
