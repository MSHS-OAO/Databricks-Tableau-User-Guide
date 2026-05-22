# What is a Catalog?

A **catalog** is the top level of the three-level namespace in Databricks:

```
catalog . schema . table
```

Every table, view, volume, and function lives inside a schema, and every schema lives inside a catalog. When you write a SQL query or reference a table in Python, you always address it with all three levels:

```sql
SELECT * FROM datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw;
```

```python
df = spark.table("datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw")
```

## Catalog Layers

| Catalog | Purpose |
|---|---|
| `datahub_dev_bronze` | Raw ingested data, unmodified from source |
| `datahub_dev_silver` | Cleaned and joined data |
| `datahub_dev_gold` | Aggregated, report-ready data |

Bronze is the landing zone — data arrives here first, exactly as it came from the source system. Silver applies transformations and quality rules. Gold contains final business metrics.

## Viewing Catalogs

In the Databricks UI, open the **Catalog** icon in the left sidebar. This opens the Catalog Explorer, where you can browse all catalogs, schemas, and tables your account has access to.

To list catalogs in SQL:

```sql
SHOW CATALOGS;
```

To list schemas inside a catalog:

```sql
SHOW SCHEMAS IN datahub_dev_bronze;
```

## Permissions

Access to a catalog is governed by Catalog permission grants:

```sql
-- Allow a user to query all tables in a schema
GRANT SELECT ON SCHEMA datahub_dev_bronze.scorecards_raw_files TO `user@mssm.edu`;

-- Allow a user to write to a volume
GRANT WRITE VOLUME ON VOLUME datahub_dev_bronze.scorecards_raw_files.finance
TO `user@mssm.edu`;

-- Allow a user to create tables in a schema
GRANT CREATE TABLE ON SCHEMA datahub_dev_bronze.scorecards_raw_files TO `user@mssm.edu`;
```

Only workspace admins and catalog owners can grant these privileges.
