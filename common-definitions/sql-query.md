# What is a SQL Query?

A **SQL query** is a statement that retrieves or modifies data in a table. In Databricks, SQL runs against Delta tables stored in Unity Catalog.

## Where to Write SQL

**SQL Editor** (recommended for ad-hoc work):
1. Click **SQL Editor** in the Databricks sidebar
2. Select a SQL Warehouse from the dropdown (top right)
3. Write your query and press `Ctrl + Enter` (or click **Run**)

**Notebook cell** (recommended when mixing SQL with Python):
```sql
%sql
SELECT * FROM datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw LIMIT 10;
```

## Basic Query Structure

```sql
SELECT column1, column2
FROM catalog.schema.table
WHERE condition
ORDER BY column1
LIMIT 100;
```

Example against a Unity Catalog table:

```sql
SELECT
    department,
    COUNT(*) AS row_count,
    SUM(budget) AS total_budget
FROM datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw
WHERE fiscal_year = 2024
GROUP BY department
ORDER BY total_budget DESC;
```

## Common Operations

### Preview a table

```sql
SELECT * FROM datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw LIMIT 20;
```

### Check row count

```sql
SELECT COUNT(*) FROM datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw;
```

### Show schema (column names and types)

```sql
DESCRIBE TABLE datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw;
```

### List all tables in a schema

```sql
SHOW TABLES IN datahub_dev_bronze.scorecards_raw_files;
```

### Create a table from a query result

```sql
CREATE OR REPLACE TABLE datahub_dev_silver.scorecards.bsc_finance_clean AS
SELECT
    department,
    TRIM(cost_center) AS cost_center,
    CAST(budget AS DOUBLE) AS budget
FROM datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw
WHERE budget IS NOT NULL;
```

## Delta-Specific Features

Because Databricks tables use Delta format, you get extra capabilities:

```sql
-- See table history (who changed what and when)
DESCRIBE HISTORY datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw;

-- Query a past version of the table
SELECT * FROM datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw VERSION AS OF 3;

-- Restore the table to a previous version
RESTORE TABLE datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw TO VERSION AS OF 3;
```

## SQL Warehouses

SQL queries in the SQL Editor need a **SQL Warehouse** (also called a compute cluster for SQL). To start one:

1. Go to **SQL Warehouses** in the sidebar
2. Click **Start** on an existing warehouse, or create a new one
3. Serverless warehouses start in seconds; classic warehouses take 1–3 minutes

Warehouse cost is based on DBU consumption while running — stop it when not in use.
