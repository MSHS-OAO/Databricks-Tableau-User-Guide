# Naming Conventions

[Back to Table of Contents](../../README.md#table-of-contents)

Consistent names make it easier for the whole team to find, understand, and maintain shared assets. Apply these rules to every Catalog object, notebook, job, and volume you create.

## General Rule

Use **lowercase letters and underscores** for all Databricks-managed assets. No spaces, no camelCase, no hyphens.

```text
catalog.schema.table
datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw
```

## Catalog Objects

| Object | Convention | Example |
|---|---|---|
| Catalog | Environment + purpose | `datahub_dev_bronze` |
| Schema | Domain or project | `scorecards_raw_files` |
| Table | Describes the data | `bsc_finance_raw` |
| Volume | Describes the file landing area | `finance` |

**Include the business area or project name** in any asset that multiple people will use. This makes the Catalog Explorer readable without needing to open every object.

**Good**: `datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw`
**Avoid**: `dheeraj_test.data.table1`

## Separating Raw and Transformed Data

Keep raw file landing areas separate from transformed [Delta Tables](../../Common%20Definitions.md#delta-table):

- Raw, unmodified source data → Bronze catalog (`datahub_dev_bronze`)
- Cleaned, joined, business-rule applied → Silver catalog (`datahub_dev_silver`)
- Aggregated, report-ready → Gold catalog (`datahub_dev_gold`)

Do not write transformed data into a Bronze schema or raw files into a Silver schema.

## Notebooks

Store notebooks that belong to a shared workflow in a shared workspace folder, not in a personal `/Users/name@...` folder.

| Location | Use for |
|---|---|
| `/Workspace/Users/name@mssm.edu/` | Personal exploration and drafts |
| `/Workspace/Shared/` | Production notebooks used by jobs or by the team |

Name notebooks after the process they run, not the person who wrote them:

**Good**: `bsc_finance_ingest`, `oracle_hr_sync`
**Avoid**: `dheeraj_notebook`, `test_v3_final`

## Jobs

Name jobs after the pipeline they execute:

**Good**: `bsc_finance_ingest`, `oracle_daily_sync`
**Avoid**: `job1`, `my_job`

Include the business area so jobs are identifiable in the Workflows list without clicking into each one.

## Volumes

Name volumes after the data domain and file type they hold:

**Good**: `finance`, `hr_extracts`, `oracle_wallet`
**Avoid**: `files`, `temp`, `uploads`

The full path should read like a description:
```
/Volumes/datahub_dev_bronze/scorecards_raw_files/finance/
```
