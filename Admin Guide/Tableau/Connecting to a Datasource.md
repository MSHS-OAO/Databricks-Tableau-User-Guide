# Connecting to a Datasource

[Back to Table of Contents](../../README.md#table-of-contents)

## What Is a Tableau Datasource?

A Tableau [Datasource](../../Common%20Definitions.md#tableau-terms) is the reusable connection layer between Tableau and the data it analyzes. It stores the connection details, selected tables or custom SQL, joins or relationships, calculated fields, metadata, and whether Tableau should query the data live or use an extract.

For our team, a Tableau datasource should point to a Databricks when possible. We wil also be able to connect to Oracle and Sharepoint files as needed. Published [datasources](../../Common%20Definitions.md#tableau-terms) should live in the specific dashboard project folder that the datasource supports. Treat shared datasources as managed assets and give them clear names.

### Connecting to Databricks

1. Within Tableau, navigate to the project folder you would like to publish data under. Make sure the project subfolder has been created under the `Health System Operations (HSO)` team project. Select the `New` dropdown and select `Published Data Source`.

<img src="../../images/new published data source.PNG" width="500">

2. Navigate to the `Connectors` option and select `Databricks`.

<img src="../../images/databricks connector.PNG" width="600">

3. Now log in to Databricks and navigate to the SQL warehouses under the compute section. Select `Severless Starter Warehouse` and navigate to the connection details. (Note no screenshots will be shared for this step to hide secure information). Here you will find the `Server Hostname` and `HTTP Path`. In Tableau make sure you select `Personal access token` for the Authentication drop down option. Paste the Tableau personal access token in the token field. Select Sign In.

4. Once the connection to Databricks has been made, navigate to the Catalog drop down on the left hand pane and search for `opsanalytics_adb_workspace01`

<img src="../../images/ops analytics catalog.PNG" width="500">

5. Search for your desired `schema` under the Database dropdown.

<img src="../../images/ops analytics schema.PNG" width="500">

6. Search for your desired `table` under the Table dropdown. Select the table you desire. Please refer to [Extract vs. Live Connection](Extract%20vs.%20Live%20Connection.md) to understand the difference between a live connection and an extract. Please refer to [Publishing Tableau Dataset](Publishing%20Tableau%20Dataset.md) for how to publish the table and make it available for the team.

<img src="../../images/ops analytics table.PNG" width="500">

### Connecting to Oracle

1. Within Tableau, navigate to the project folder you would like to publish data under. Make sure the project subfolder has been created under the `Health System Operations (HSO)` team project. Select the `New` dropdown and select `Published Data Source`.

<img src="../../images/new published data source.PNG" width="500">

2. Navigate to the `Connectors` option and select `Oracle`.

<img src="../../images/oracle connector.PNG" width="600">

3. For the `Server` input, paste `ADWDBTST_LOW`. Enter `OAO_PRODUCTION` as the `Username` and paste the password.

<img src="../../images/oracle credentials.PNG" width="600">

4. Once the connection to Databricks has been made, navigate to the `Schema` drop down on the left hand pane and search for `OAO_PRODUCTION` and select it.

<img src="../../images/oao prod schema.PNG" width="500">

5. Search for your desired `Table` under the Table dropdown and select it.

<img src="../../images/oao prod table.PNG" width="500">

6. Please refer to [Extract vs. Live Connection](Extract%20vs.%20Live%20Connection.md) to understand the difference between a live connection and an extract. Please refer to [Publishing Tableau Dataset](Publishing%20Tableau%20Dataset.md) for how to publish the table and make it available for the team.

### Connecting to Sharepoint/Onedrive

1. Within Tableau, navigate to the project folder you would like to publish data under. Make sure the project subfolder has been created under the `Health System Operations (HSO)` team project. Select the `New` dropdown and select `Published Data Source`.

<img src="../../images/new published data source.PNG" width="500">

2. Navigate to the `Connectors` option and select `OndeDrive and SharePoint Online` and sign in with the default URL provided. This will send you to the Mount Sinai SSO.

<img src="../../images/sharepoint connector.PNG" width="600">

3. Navigate to the desired file

4. Please refer to [Extract vs. Live Connection](Extract%20vs.%20Live%20Connection.md) to understand the difference between a live connection and an extract. Please refer to [Publishing Tableau Dataset](Publishing%20Tableau%20Dataset.md) for how to publish the table and make it available for the team.
