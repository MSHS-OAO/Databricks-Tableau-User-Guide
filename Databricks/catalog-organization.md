# Catalog Organization — Schema vs Table vs Volume

[Back to Table of Contents](../README.md#table-of-contents)

Every piece of data in Databricks sits inside a three-level hierarchy. Understanding when to use each level keeps pipelines organized and permissions manageable.

## The Hierarchy

```
Catalog
  └── Schema
        ├── Table   (queryable Delta dataset)
        └── Volume  (raw file storage)
```

Full address format: `catalog.schema.table` or `/Volumes/catalog/schema/volume/`

## Catalogs — Separate Environments and Governance Boundaries

Use separate catalogs to isolate environments or major data ownership boundaries.

| Catalog | Purpose |
|---|---|
| `datahub_dev_bronze` | Raw ingested data, unmodified from source |
| `datahub_dev_silver` | Cleaned, joined, and business-rule-applied data |
| `datahub_dev_gold` | Aggregated, report-ready data for Tableau |

Data flows left to right: source systems → Bronze → Silver → Gold → Tableau.

Never write processed data into Bronze, and never land raw files into Silver or Gold.

## Schemas — Group by Domain or Pipeline Stage

A [Schema](../Common%20Definitions.md#schema) lives inside a catalog and groups related datasets. Use schemas to organize by business domain, project, or pipeline stage.

Examples:

| Schema | What it holds |
|---|---|
| `datahub_dev_bronze.scorecards_raw_files` | Raw scorecard uploads and their ingestion volumes |
| `datahub_dev_silver.scorecards` | Cleaned scorecard tables ready for joining |
| `datahub_dev_bronze.oracle_raw` | Tables read directly from Oracle source systems |

Create a new schema when a group of tables and volumes belongs to a distinct project or data domain.

## Tables — Queryable Delta Datasets

A [Table](../Common%20Definitions.md#table) is the output of a transformation step. It is queryable with SQL and directly consumable by Tableau.

Rules:
- Tables live inside a schema: `datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw`
- Always use Delta format (the Databricks default)
- Write with `mode("overwrite")` or `mode("append")` depending on the pipeline design
- Use `.option("overwriteSchema", "true")` when upstream column names can change between runs

## Volumes — Raw File Storage

A [Volume](../Common%20Definitions.md#volume) holds raw files before they are read into a table. Think of it as a managed folder inside a schema.

Rules:
- Volumes live inside a schema: `/Volumes/datahub_dev_bronze/scorecards_raw_files/finance/`
- Use volumes as the landing zone for files uploaded via Power Automate, SFTP, or manual upload
- Never query a volume directly with SQL — read the file into a DataFrame first, then write it as a table
- Grant only the permissions required: `WRITE VOLUME` for upload pipelines, `READ VOLUME` for ingestion jobs

## Always Use Full Object Names

When writing SQL or Python that references a Catalog object, always use the full three-level name. Never rely on a `USE CATALOG` or `USE SCHEMA` statement that might not be set in every context.

**Good**:
```sql
SELECT * FROM datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw;
```
```python
df = spark.table("datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw")
```

**Avoid**:
```sql
USE SCHEMA scorecards_raw_files;
SELECT * FROM bsc_finance_raw;  -- breaks when catalog context is different
```

## Granting Access

Access is controlled at each level. Grant the minimum privilege required:

```sql
-- Read a table
GRANT SELECT ON TABLE datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw TO `user@mssm.edu`;

-- Upload files to a volume
GRANT WRITE VOLUME ON VOLUME datahub_dev_bronze.scorecards_raw_files.finance TO `user@mssm.edu`;

-- Create new tables in a schema
GRANT CREATE TABLE ON SCHEMA datahub_dev_silver.scorecards TO `user@mssm.edu`;
```

Only workspace admins and catalog owners can run `GRANT` statements.
