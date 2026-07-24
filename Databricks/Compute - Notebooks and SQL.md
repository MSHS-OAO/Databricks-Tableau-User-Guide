# Compute - Notebooks and SQL

[Back to Table of Contents](../README.md#table-of-contents)

All code is executed in Databricks by something called [compute](../Common%20Definitions.md#databricks-terms). Only admins are able to create [compute](../Common%20Definitions.md#databricks-terms) and they are responsible for sharing it with the rest of the team. When a new workflow needs [compute](../Common%20Definitions.md#databricks-terms), coordinate with the admins so the right option is selected.

## Compute Types

We use two main [compute](../Common%20Definitions.md#databricks-terms) types:

- **[All-purpose compute](../Common%20Definitions.md#databricks-terms)**: Optimized for [notebooks](../Common%20Definitions.md#databricks-terms) with mixed language coding (SQL + Python + R)
- **[SQL warehouses](../Common%20Definitions.md#databricks-terms)**: Optimized for SQL queries. Used within the SQL Editor

Our team has 3 [all-purpose compute](../Common%20Definitions.md#databricks-terms) options:
```text
Serverless
OAO_DEVELOPMENT Compute
OAO_PRODUCTION Compute
```

Our team has 2 [SQL warehouse](../Common%20Definitions.md#databricks-terms) [compute](../Common%20Definitions.md#databricks-terms) options:
```text
Serverless Starter Warehouse
OAO_DEVELOPMENT SQL Warehouse
```

<u>**Team Guidelines**</u>: When possible, always use a SQL editor to explore/analyze data. Serverless SQL Starter Warehouse will be used for all SQL queries in the SQL editor during data exploration. Notebooks will be used in 3 main scenarios: visualizing data, querying Oracle DB, and complex analysis that SQL can't do. For development in notebooks we will primarily use `OAO_DEVELOPMENT Compute`. For production code, the [compute](../Common%20Definitions.md#databricks-terms) choice will be made case by case depending on the needs of the code.

## SQL Editor

An example SQL Editor code is stored here: [Query Example](../Code%20Examples/Query%20Example.dbquery.ipynb)

SQL Editors should be your first option for data analysis. They are best for data exploration and when you want to quickly export a file out of Databricks as `csv` or `excel`. There are two primary ways to start a SQL Editor:
1. The easiest method is to select the SQL Editor button underneath the SQL section of the left-hand navigation pane. This will open a recent SQL Editor if you have one or prompt you to create one. If you are prompted to create one, it will default to your personal drafts folder.

<img src="../images/sql editor.PNG"> 

2. The second option, if you know where you want the SQL file to exist in the workspace, is to navigate to that location and create a SQL file from that location.

<img src="../images/sql editor folder.PNG" height="1000"> 

Now that you have created a SQL query file, there are two things to do before you start writing SQL.

<img src="../images/sql editor architecture.PNG" height="1000">

1. Select the [catalog](../Common%20Definitions.md#databricks-terms) and [schema](../Common%20Definitions.md#databricks-terms) you want to work in. This example is using the team [catalog](../Common%20Definitions.md#databricks-terms) and the default [schema](../Common%20Definitions.md#databricks-terms).
2. Attach a [SQL warehouse](../Common%20Definitions.md#databricks-terms) to the SQL Editor. This example uses the serverless starter warehouse. Reminder, in most cases this is the [compute](../Common%20Definitions.md#databricks-terms) you should be selecting.

It is convenient to select the [catalog](../Common%20Definitions.md#databricks-terms) and [schema](../Common%20Definitions.md#databricks-terms) of the data you will be querying. In the example below, the [catalog](../Common%20Definitions.md#databricks-terms) and [schema](../Common%20Definitions.md#databricks-terms) were changed to `datahub_dev_bronze` and `msx`, respectively. Now in the `FROM` clause, we do not need to specify [catalog](../Common%20Definitions.md#databricks-terms) or [schema](../Common%20Definitions.md#databricks-terms).

<img src="../images/sql editor architecture - workspace change.PNG" width="1000"> 

## Notebooks

An example notebook is stored here: [notebook](../Code%20Examples/Notebook%20Example.ipynb)

[Notebooks](../Common%20Definitions.md#databricks-terms) are used for multi-language coding or anything that requires something other than SQL. Create a [notebook](../Common%20Definitions.md#databricks-terms) from the desired location in the [workspace](../Common%20Definitions.md#databricks-terms) by navigating to that folder and selecting Notebook from the Create dropdown in the top right.

<img src="../images/create notebook.PNG" width="1000">

Similarly, we must attach [compute](../Common%20Definitions.md#databricks-terms) to the [notebook](../Common%20Definitions.md#databricks-terms), which will most often be `OAO_DEVELOPMENT Compute`. Here is an example of a simple [notebook](../Common%20Definitions.md#databricks-terms) that uses a SQL chunk and a Python chunk. Notice that the data from the SQL chunk is passed to the Python chunk using `_sqldf`.

<img src="../images/simple notebook.PNG" width="1000">

## Sharing Code

Any code created and committed in a [Git folder](../Common%20Definitions.md#databricks-terms) will be shared with the team automatically.

Anything you create in a personal [workspace](../Common%20Definitions.md#databricks-terms) is only visible to you. If desired, you will need to share it specifically with a team member. Alternatively, you can share it with all users if you want the entire team to have access. From the [notebook](../Common%20Definitions.md#databricks-terms) or SQL Editor, you can select the share button in the top right corner. Add individuals or `All workspace users` for the entire team. You also have the ability to modify their permission level when sharing:
1. **Can Manage**: user can do anything to the file. This is the highest level of access. Edit, run, view, change [compute](../Common%20Definitions.md#databricks-terms), delete, share. Be careful when selecting this option.
2. **Can Edit**: user can edit the code within the file and run it. This is the most permissions you can grant a user without giving them full ownership of the file.
3. **Can Run**: user can only run the code in the file. They can't change the code itself.
4. **Can View**: user can only see the file but they can't run the code.
