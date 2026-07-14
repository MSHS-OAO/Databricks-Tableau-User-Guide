# GitHub Conventions

[Back to Table of Contents](../README.md#table-of-contents)

[Git folders](../Common%20Definitions.md#databricks-terms) will be used as the standard convention for version control of all project work. Personal [workspace](../Common%20Definitions.md#databricks-terms) folders are fine for early exploration. You can create whatever folders or files in your personal [workspace](../Common%20Definitions.md#databricks-terms). Production [notebooks](../Common%20Definitions.md#databricks-terms), shared SQL, [job](../Common%20Definitions.md#databricks-terms) code, and project documentation should live in a shared Git-backed project.

## Creating Git Folders

A [Git folder](../Common%20Definitions.md#databricks-terms) is a Databricks [workspace](../Common%20Definitions.md#databricks-terms) folder that is specifically connected to a Git repository. We will create our [Git folders](../Common%20Definitions.md#databricks-terms) in the shared location on the [workspace](../Common%20Definitions.md#databricks-terms) so all users can access the folder and make changes to the repo. Note that a [Git folder](../Common%20Definitions.md#databricks-terms) only needs to be created once.

Within the [workspace](../Common%20Definitions.md#databricks-terms), navigate to the `shared` folder, select create, then select [Git folder](../Common%20Definitions.md#databricks-terms).

<img src="../images/git folder.PNG" width="1000">

Paste the Git repo URL and select create [Git folder](../Common%20Definitions.md#databricks-terms).

<img src="../images/create git folder.PNG" width="1000">

## Branching In Databricks

Now that the [Git folder](../Common%20Definitions.md#databricks-terms) has been created, we can view the branch to the right of the repo name. Click on the branch to enter the Git UI where we can change branches or create a new branch.

<img src="../images/select branch.PNG" width="1000">

Similarly, we can select the three ellipses and select `Git...` to enter the same Git UI.

<img src="../images/enter git for changes.PNG" width="1000">

## Committing In Databricks

After editing [notebooks](../Common%20Definitions.md#databricks-terms), SQL files, or supporting project files in the Databricks [Git folder](../Common%20Definitions.md#databricks-terms), enter the Git UI by using either method mentioned in the branching section. The first time you commit or push to GitHub, you will need to add your Git credential. This links your GitHub account to Databricks and allows commits and pushes to flow from Databricks to GitHub. Navigate to the settings tab, select the dropdown under Git credential, and select Add Git credential. Change the nickname of the credential to `GitHub - <your name>`. Make sure the Link Git account option is selected and select Link. Now in the Git credential dropdown, you should see your credential. Select it and hit save.

<img src="../images/git credential.PNG" width="700">

Review the changed files before committing. Commit only the files that belong to the current change.

<img src="../images/commit example.PNG" width="1000">

## Pushing From Databricks

After committing, a push can be made from the same Git UI. A commit that has not been pushed is still only available from the Databricks [Git folder](../Common%20Definitions.md#databricks-terms) where it was created.

## Pulling Into Databricks

Before starting new work in a shared [Git folder](../Common%20Definitions.md#databricks-terms), pull the latest changes in Databricks. Pull again before committing if other team members may have updated the same project.

If Databricks reports a conflict during pull, stop and review the conflicting files before continuing. Do not overwrite another team member's work unless the team has agreed that the change should be replaced.
