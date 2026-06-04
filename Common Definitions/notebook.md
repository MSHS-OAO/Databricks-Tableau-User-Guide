# What is a Notebook?

A **Databricks notebook** is an interactive document where you write and run code in cells. Notebooks support Python, SQL, Scala, and R — and you can mix languages in the same notebook using magic commands.

## Creating a Notebook

1. In the Databricks sidebar, click **New → Notebook**
2. Give it a name and choose a default language (Python is most common)
3. The notebook opens with one empty cell

## Running Cells

- **Run one cell**: Click the play button (▶) on the left of the cell, or press `Shift + Enter`
- **Run all cells**: Click **Run all** in the toolbar
- Output appears directly below each cell

## Magic Commands

Switch languages inside a Python notebook with magic commands at the top of a cell:

```python
# Default cell — Python
df = spark.table("datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw")
df.show()
```

```sql
%sql
-- SQL cell
SELECT COUNT(*) FROM datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw;
```

```python
%md
# This cell renders as Markdown documentation
```

## Widgets (Parameters)

Widgets let a notebook accept input — either from the UI or from a Databricks [Job](../Common%20Definitions.md#job). This is how [Power Automate](../Common%20Definitions.md#power-automate) passes a filename to a notebook at runtime.

```python
# Declare a widget with a default value
dbutils.widgets.text("file_name", "default_file.xlsx")

# Read the value (works whether set by UI or job_parameters)
file_name = dbutils.widgets.get("file_name")
print(f"Processing: {file_name}")
```

When a job runs the notebook, the `job_parameters` dict in the API call overrides the default:

```json
{
  "job_parameters": {
    "file_name": "OAO_PRODUCTION_BSC_FINANCE_TABLE.xlsx"
  }
}
```

## Installing Packages

If a library is not on the cluster, install it at the top of the notebook:

```python
%pip install openpyxl
dbutils.library.restartPython()
```

The `restartPython()` call is required after `%pip` so the newly installed package is available in subsequent cells.

## Saving and Sharing

Notebooks are saved automatically. To share:

- Click **Share** in the top-right corner
- Add a user or group and choose **Can View**, **Can Comment**, or **Can Edit**

## Where Notebooks Live

Notebooks are stored in the Workspace, not in Catalog. The path looks like:

```
/Workspace/Users/user@mssm.edu/notebook_name
```

When attaching a notebook to a Databricks Job, you reference this workspace path.
