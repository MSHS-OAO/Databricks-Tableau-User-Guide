# Databricks Organization

Databricks organizes data and work across several layers. Understanding these layers makes it easier to know where data lives, how to reference it, and how [Tableau](../Common%20Definitions.md#tableau) will connect to it later. This section will review how Databricks organizes its components and how we will integrate them into our workflow.

## Workspace

A [workspace](../Common%20Definitions.md#workspace) is the Databricks environment where users write [notebooks](../Common%20Definitions.md#notebook), write SQL queries, run [jobs](../Common%20Definitions.md#job), and access data. The workspace is where the team does the actual work, but the data itself is organized through [Catalog](../Common%20Definitions.md#catalog) objects such as catalogs, schemas, tables, and volumes.

## Catalog

A [catalog](../Common%20Definitions.md#catalog) is the top-level container for data in Databricks. Our team is given a single catalog and DTP owns several catalogs that they populate with data. For comparison, Oracle Cloud as a whole is essentially at the same hierarchy as a catalog in Databricks.

We will primarily work with 2 catalogs:
```text
opsanalytics_adb_workspace01
```
This is our team's catalog. It is tied to our workspace and conveniently shares the same name as our workspace, which is shown in the top right corner of your Databricks screen (`opsanalytics-adb-workspace01`). This catalog is where our team will store our project data.

```text
datahub_dev_bronze
```
This is the DTP catalog where we will be able to access many of our source tables including MSX and Clarity data.

## Schema

A [schema](../Common%20Definitions.md#schema) is a container inside a catalog. Within a schema are grouped tables and volumes. Our team will create a new schema for every project we engage in. As stated in the catalog section, all of our team's schemas will live inside of `opsanalytics_adb_workspace01`. For comparison, `OAO_PRODUCTION` and `OAO_DEVELOPMENT` within Oracle Cloud are at the same hierarchy level as the schema level in Databricks.  

Most source data in `datahub_dev_bronze` will primarily live under these schemas:

```text
msx
clarity
```

## Table

A [table](../Common%20Definitions.md#table) is a queryable dataset inside a schema. Tables are what users query with SQL and what Tableau will connect to for reporting.

Use the full three-part name when documenting or querying a table:

```text
catalog.schema.table
```

Example:

```text
SELECT *
FROM datahub_dev_bronze.msx.msx_ip_output;
```

## Volume

A [volume](../Common%20Definitions.md#volume) is a file storage location inside a catalog. Volumes will be used for two purposes on our team.

1. A location for files (`.xlsx` or `.csv`) to be placed as a staging area before they are turned into tables.
2. A location for saving files produced by a model or analysis.
