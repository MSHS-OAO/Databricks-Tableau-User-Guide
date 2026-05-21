# Databricks Organization

Databricks organizes data and work across several layers. Understanding these layers makes it easier to know where data lives, how to reference it, and how [Tableau](../Common%20Definitions.md) will connect to it later. This section will review how Databricks organizes its components and how we will integrate them into our workflow.

## Workspace

A [workspace](../Common%20Definitions.md) is the Databricks environment where users write [notebooks](../Common%20Definitions.md), write SQL queries, run [jobs](../Common%20Definitions.md), and access data. The workspace is where the team does the actual work, but the data itself is organized through [Catalog](../Common%20Definitions.md) objects such as catalogs, schemas, tables, and volumes.

## Catalog

A [catalog](../Common%20Definitions.md) is the top-level container for data in Databricks. Our team is given a single catalog and DTP owns several catalogs that they populate with data. For comparison, Oracle Cloud as a whole is essentially at the same hierarchy as a catalog in Databricks.

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

A [schema](../Common%20Definitions.md) is a container inside a catalog. Within a schema are grouped tables and volumes. Our team will create a new schema for every project we engage in. As stated in the catalog section, all of our team's schemas will live inside of `opsanalytics_adb_workspace01`. For comparison, `OAO_PRODUCTION` and `OAO_DEVELOPMENT` within Oracle Cloud are at the same hierarchy level as the schema level in Databricks.  

Most source data in `datahub_dev_bronze` will primarily live under these schemas:

```text
msx
clarity
```

## Table

A [table](../Common%20Definitions.md) is a queryable dataset inside a schema. Tables are what users query with SQL and what Tableau will connect to for reporting.

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

A [volume](../Common%20Definitions.md) is a file storage location inside a catalog. Volumes will be used for two purposes on our team.

1. A location for files (`.xlsx` or `.csv`) to be placed as a staging area before they are turned into tables.
2. A location for saving files produced by a model or analysis.

## GitHub Conventions

[Git folders](../Common%20Definitions.md) will be used as the standard convention for version control of all project work. Personal workspace folders are fine for early exploration, but production notebooks, shared SQL, job code, and project documentation should live in a shared GitHub-backed project.

### Creating Git Folders

A [Git folder](../Common%20Definitions.md) is a Databricks workspace folder that is connected to GitHub. Create Git folders in a team or project workspace location rather than inside a personal folder when the work is expected to support a shared project.

In Databricks, create or open Git folders from the workspace file browser. Use the Git folder option to connect the Databricks folder to the correct GitHub project, then confirm the folder opens with Git controls available at the top of the page.

### Branching In Databricks

Use the branch selector in the Databricks Git folder before making changes. Create or switch to a working branch when the change is not ready for the shared version of the project.

### Committing In Databricks

After editing notebooks, SQL files, or supporting project files in the Databricks Git folder, use the Git controls to review the changed files before committing. Commit only the files that belong to the current change.

Commit messages should describe the workflow or business change, not just the file that changed.

### Pushing From Databricks

After committing, push the change from Databricks so the update is saved back to GitHub. A commit that has not been pushed is still only available from the Databricks Git folder where it was created.

Push before asking another team member to review the work or before expecting the change to be available outside of your Databricks session.

### Pulling Into Databricks

Before starting new work in a shared Git folder, pull the latest changes in Databricks. Pull again before committing if other team members may have updated the same project.

If Databricks reports a conflict during pull, stop and review the conflicting files before continuing. Do not overwrite another team member's work unless the team has agreed that the change should be replaced.