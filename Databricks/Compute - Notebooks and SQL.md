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

An example SQL Editor code is stored here: [Query Example](../Code%20Examples/Query%20Example.dbquery.ipynb)

SQL Editors are used when you only need to write SQL. Best for data exploration and when you want to quickly export a file out of databricks as `csv` or `excel`. There are two primary ways to start a SQL editor
1. The easiest method is to select the SQL Editor button underneath the SQL section of left hand navigation pane. This will open up a recent SQL editor if you have one or prompt you to create one. If you are prompted to create one, it will default to create in your personal drafts folder.

<img src="../images/sql editor.PNG" alt="Create Git folder dialog"> 

2. The second option, if you know where you want the SQL file to exist, is to navigate to that location and create a SQL file from that location.

<img src="../images/sql editor folder.PNG" alt="Create Git folder dialog" width="1000"> 

Now that you have created a SQL query file, theres are two things to do before you start writing SQL.

<img src="../images/sql editor architecture.PNG" alt="Create Git folder dialog" width="1000"> 

1. Select the catalog and schema you want to work in. This example is using the team catalog and the default schema.
2. Attach a [SQL warehouse](../Common%20Definitions.md) to the SQL editor. This example uses the serverless starter warehouse. Reminder, in most cases this is the compute you should be selecting.

Note that is convenient to select the catalog and schema of the data you will be querying. In the below example, the catalog and schema were changed to datahub_dev_bronze and msx respectively. Now in the `FROM` clause we do not need to specify catalog or schema.

<img src="../images/sql editor architecture - workspace change.PNG" alt="Create Git folder dialog" width="1000"> 

## Notebooks

An example notebook is stored here: [notebook](../Code%20Examples/Notebook%20Example.ipynb)

Notebooks are used for multi-language coding or anything that does not use SQL. Create a notebook from the desired location in the workspace by navigating to that folder and selected Notebook from the Create dropdown in the top right.

<img src="../images/create notebook.PNG" alt="Create Git folder dialog" width="1000">

Similarly we must attach a compute to the notebook which we will most often use `Severless`. Here is an example of a simple notebook that uses an SQL chunk and a python chunk. Notice that the data from the SQL chunk is passed to the python chunk using `_sqldf`

<img src="../images/simple notebook.PNG" alt="Create Git folder dialog" width="1000">

## Sharing Code

Any code created and commited in a git folder will be shared with the team automaticall.

Anything you create in a personal workspace is only visible to you. If desired you will need to share it specifically with a teammember. Alternatively you can share it will all users if you want the entire team to have access. From the notebook or SQL editor, you can select the share buttom in the top right corner. Add individuals or `All workspace users` for the entire team. You also have the ability to modify their permissions level when sharing:
1. **Can Manage**: user can do anything to the file. This is the highest level of access. Edit, run, view, change compute, delete, share. Be careful when selecting this option.
2. **Can Edit**: user can edit the code within the file and run it. This is the most permissions you can grant a user without giving them full ownership of the file.
3. **Can Run**: user can only run the code in the file. They can't change the code itself.
4. **Can View**: user can only see the file but they can't run the code.
