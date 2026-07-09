# Publishing a Tableau Dataset

[Back to Table of Contents](../../README.md#table-of-contents)

## Check Connection Type

Before publishing, make sure you have selected the desired connection type. Please review [Extract vs. Live Connection](Extract%20vs.%20Live%20Connection.md) for best practices on what selection to make.

1. If you have chosen to use a [live connection](../../Common%20Definitions.md#tableau-terms), make sure the `Live` bubble has been selected in the top right corner.

<img src="../../images/live connection.PNG" width="500">

2. If you have chosen to use an [extract](../../Common%20Definitions.md#tableau-terms) connection, select the `Extract` bubble and select Create Extract. The [extract](../../Common%20Definitions.md#tableau-terms) can take several minutes to load.

<img src="../../images/extract.PNG" width="500">

3. Now you must select the `Publish As...` button in the top right. Make sure you are publishing the [datasource](../../Common%20Definitions.md#tableau-terms) to the correct project folder. Make sure you check the embed credentials box (this will ensure that team members do not have to submit the connection credentials every time they use the [datasource](../../Common%20Definitions.md#tableau-terms)). Our standard naming convention applies here as well, and it is best practice to name the [datasource](../../Common%20Definitions.md#tableau-terms) exactly how the [table](../../Common%20Definitions.md#databricks-terms) or file is named to avoid confusion. Finally, select publish. Refreshing the project folder should show the [datasource](../../Common%20Definitions.md#tableau-terms) now.

4. For [extract](../../Common%20Definitions.md#tableau-terms) connections, you will most likely want to select a refresh cadence. Select the three ellipses and select `Refresh Extracts Now...` if you would like to manually refresh the [datasource](../../Common%20Definitions.md#tableau-terms). If you want to create a refresh cadence, select `Refresh Extracts...`. Select the desired refresh cadence from the list of options and select `Schedule Refresh`.

<img src="../../images/refresh cadence.PNG" width="500">

<img src="../../images/schedule refresh.PNG" width="500">
