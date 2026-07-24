# Databricks Architecture

[Back to Table of Contents](../README.md#table-of-contents)

Databricks organizes data and work across several layers. Understanding these layers makes it easier to know where data lives, how to reference it, and how Tableau will connect to it later. This section reviews how Databricks organizes its components and how we will integrate them into our workflow.

## Workspace

A [workspace](../Common%20Definitions.md#databricks-terms) is the Databricks environment where users write [notebooks](../Common%20Definitions.md#databricks-terms), write SQL queries, run [jobs](../Common%20Definitions.md#databricks-terms), and access data. The workspace acts as the file/folder structure within Databricks and it is where the team does the actual work, but the data itself is organized through [Catalog](../Common%20Definitions.md#databricks-terms) objects such as [catalogs](../Common%20Definitions.md#databricks-terms), [schemas](../Common%20Definitions.md#databricks-terms), [tables](../Common%20Definitions.md#databricks-terms), and [volumes](../Common%20Definitions.md#databricks-terms).

## Catalog

A [catalog](../Common%20Definitions.md#databricks-terms) is the top-level container for data in Databricks. Our team is given a single [catalog](../Common%20Definitions.md#databricks-terms) and DTP owns several [catalogs](../Common%20Definitions.md#databricks-terms) that they populate with data. For comparison, Oracle Cloud as a whole is essentially at the same hierarchy as a [catalog](../Common%20Definitions.md#databricks-terms) in Databricks.

We will primarily work with 2 catalogs:

```text
opsanalytics_adb_workspace01
```

This is our team's [catalog](../Common%20Definitions.md#databricks-terms). It is tied to our [workspace](../Common%20Definitions.md#databricks-terms) and conveniently shares the same name as our [workspace](../Common%20Definitions.md#databricks-terms), which is shown in the top right corner of your Databricks screen (`opsanalytics-adb-workspace01`). This [catalog](../Common%20Definitions.md#databricks-terms) is where our team will store our project data.

```text
datahub_dev_bronze
```

This is the DTP [catalog](../Common%20Definitions.md#databricks-terms) where we will be able to access many of our source [tables](../Common%20Definitions.md#databricks-terms) including `MSX` and `Clarity` data.

## Schema

A [schema](../Common%20Definitions.md#databricks-terms) is a container inside a [catalog](../Common%20Definitions.md#databricks-terms). Within a [schema](../Common%20Definitions.md#databricks-terms) are grouped [tables](../Common%20Definitions.md#databricks-terms) and [volumes](../Common%20Definitions.md#databricks-terms). Our team will create three [schemas](../Common%20Definitions.md#databricks-terms) for every project we engage in. 1 schema for mapping tables, 1 for production tables and 1 for staging. As stated in the [catalog](../Common%20Definitions.md#databricks-terms) section, all of our team's [schemas](../Common%20Definitions.md#databricks-terms) will live inside of `opsanalytics_adb_workspace01`. For comparison, `OAO_PRODUCTION` and `OAO_DEVELOPMENT` within Oracle Cloud are at the same hierarchy level as the [schema](../Common%20Definitions.md#databricks-terms) level in Databricks.

Most source data in `datahub_dev_bronze` will primarily live under these [schemas](../Common%20Definitions.md#databricks-terms):

```text
msx
clarity
```

## Table

A [table](../Common%20Definitions.md#databricks-terms) is a queryable dataset inside a [schema](../Common%20Definitions.md#databricks-terms). [Tables](../Common%20Definitions.md#databricks-terms) are what users query with SQL and what Tableau will connect to for reporting.

Use the full three-part name when documenting or querying a [table](../Common%20Definitions.md#databricks-terms):

```text
catalog.schema.table
```

Example:

```text
SELECT *
FROM datahub_dev_bronze.msx.msx_ip_output;
```

## Volume

A [volume](../Common%20Definitions.md#databricks-terms) is a file storage location inside a [schema](../Common%20Definitions.md#databricks-terms). [Volumes](../Common%20Definitions.md#databricks-terms) will be used primarily as a location for files (`.xlsx` or `.csv`) to be placed as a staging area before they are turned into [tables](../Common%20Definitions.md#databricks-terms).

**Note:** `.xlsx` or `.csv` files saved within a workbook should be saved in the workspace not as a volume.

