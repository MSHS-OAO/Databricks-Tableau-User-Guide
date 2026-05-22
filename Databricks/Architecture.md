# Databricks Architecture

[Back to Table of Contents](../README.md#table-of-contents)

Databricks organizes data and work across several layers. Understanding these layers makes it easier to know where data lives, how to reference it, and how Tableau will connect to it later. This section reviews how Databricks organizes its components and how we will integrate them into our workflow.

## Workspace

A [workspace](../Common%20Definitions.md) is the Databricks environment where users write [notebooks](../Common%20Definitions.md), write SQL queries, run [jobs](../Common%20Definitions.md), and access data. The [workspace](../Common%20Definitions.md) is where the team does the actual work, but the data itself is organized through [Catalog](../Common%20Definitions.md) objects such as [catalogs](../Common%20Definitions.md), [schemas](../Common%20Definitions.md), [tables](../Common%20Definitions.md), and [volumes](../Common%20Definitions.md).

## Catalog

A [catalog](../Common%20Definitions.md) is the top-level container for data in Databricks. Our team is given a single [catalog](../Common%20Definitions.md) and DTP owns several [catalogs](../Common%20Definitions.md) that they populate with data. For comparison, Oracle Cloud as a whole is essentially at the same hierarchy as a [catalog](../Common%20Definitions.md) in Databricks.

We will primarily work with 2 catalogs:

```text
opsanalytics_adb_workspace01
```

This is our team's [catalog](../Common%20Definitions.md). It is tied to our [workspace](../Common%20Definitions.md) and conveniently shares the same name as our [workspace](../Common%20Definitions.md), which is shown in the top right corner of your Databricks screen (`opsanalytics-adb-workspace01`). This [catalog](../Common%20Definitions.md) is where our team will store our project data.

```text
datahub_dev_bronze
```

This is the DTP [catalog](../Common%20Definitions.md) where we will be able to access many of our source [tables](../Common%20Definitions.md) including `MSX` and `Clarity` data.

## Schema

A [schema](../Common%20Definitions.md) is a container inside a [catalog](../Common%20Definitions.md). Within a [schema](../Common%20Definitions.md) are grouped [tables](../Common%20Definitions.md) and [volumes](../Common%20Definitions.md). Our team will create a new [schema](../Common%20Definitions.md) for every project we engage in. As stated in the [catalog](../Common%20Definitions.md) section, all of our team's [schemas](../Common%20Definitions.md) will live inside of `opsanalytics_adb_workspace01`. For comparison, `OAO_PRODUCTION` and `OAO_DEVELOPMENT` within Oracle Cloud are at the same hierarchy level as the [schema](../Common%20Definitions.md) level in Databricks.

Most source data in `datahub_dev_bronze` will primarily live under these [schemas](../Common%20Definitions.md):

```text
msx
clarity
```

## Table

A [table](../Common%20Definitions.md) is a queryable dataset inside a [schema](../Common%20Definitions.md). [Tables](../Common%20Definitions.md) are what users query with SQL and what Tableau will connect to for reporting.

Use the full three-part name when documenting or querying a [table](../Common%20Definitions.md):

```text
catalog.schema.table
```

Example:

```text
SELECT *
FROM datahub_dev_bronze.msx.msx_ip_output;
```

## Volume

A [volume](../Common%20Definitions.md) is a file storage location inside a [schema](../Common%20Definitions.md). [Volumes](../Common%20Definitions.md) will be used for two purposes on our team.

1. A location for files (`.xlsx` or `.csv`) to be placed as a staging area before they are turned into [tables](../Common%20Definitions.md).
2. A location for saving files produced by a model or analysis.
