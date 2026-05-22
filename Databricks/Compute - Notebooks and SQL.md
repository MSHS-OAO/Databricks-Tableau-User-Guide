# Compute - Notebooks and SQL

All code is executed in Databricks by something called [compute](../Common%20Definitions.md). Only admins are able to create [compute](../Common%20Definitions.md) and they are responsible for sharing it with the rest of the team. When a new workflow needs compute, coordinate with the admins so the right option is selected.

## Compute Types

We use two main compute types:

- **All-purpose compute**: Optimized for notebooks with mixed language coding (SQL + Python +R)
- **SQL warehouses**: Optimized for SQL queries. Used within the sql editor

Our team has 3 All-purpose Compute Options
```text
Serverless
OAO_DEVELOPMENT Compute
OAO_PRODUCTION Compute
```

Our team has 2 SQL Warehouse Compute Options
```text
Serverless Starter Warehouse
OAO_DEVELOPMENT SQL Warehouse
```

<u>**Team Guidelines**</u>: Serverless will be used for all non production code (development and data exploration). Only when the non-production code requires additional resources, we will use `OAO_DEVELOPMENT Compute` for notebooks and `OAO_DEVELOPMENT SQL Warehouse` for SQL Editor. For production code the compute choice will be on a case by case basis depending on the needs of the code.

## SQL Editor

There are two primary ways to start a SQL editor
1. The easiest method is to select the SQL Editor button underneath the SQL section of left hand navigation pane. This will open up a recent SQL editor if you have one or prompt you to create one. If you are prompted to create one, it will default to create in your personal drafts folder.

<img src="../images/sql editor.PNG" alt="Create Git folder dialog"> 

2. The second option if you know where you want the SQL file to exist is to navigate to that location and create a SQL file from that location.

<img src="../images/sql editor folder.PNG" alt="Create Git folder dialog" width="1000"> 

Now that you have created a SQL query file, theres are two things to do before you start writing SQL.

<img src="../images/sql editor architecture.PNG" alt="Create Git folder dialog" width="1000"> 

1. Select the catalog and schema you want to work in. This example is using the team catalog and the default schema.
2. SAttach a [SQL warehouse](../Common%20Definitions.md) to the SQL editor. This example uses the serverless starter warehouse. Reminder, in most cases this is the compute you should be selecting.

Note that is convenient to select the catalog and schema of the data you will be querying. In the below example, the catalog and schema were changed to datahub_dev_bronze and msx respectively. Now in the `FROM` clause we do not need to specify catalog or schema.

<img src="../images/sql editor architecture - workspace change.PNG" alt="Create Git folder dialog" width="1000"> 

## Notebooks

Attach compute to a notebook based on the work being done:

- Use [all-purpose compute](../Common%20Definitions.md) for exploratory notebook work.
- Use serverless when it is sufficient for the notebook's workload.
- Use [job compute](../Common%20Definitions.md) when the notebook is part of a scheduled production workflow that needs a predictable runtime environment.

