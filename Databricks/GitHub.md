# GitHub Conventions

[Git folders](../Common%20Definitions.md) will be used as the standard convention for version control of all project work. Personal [workspace](../Common%20Definitions.md) folders are fine for early exploration. You can create whatever folders/files in your personal location in your personal [workspace](../Common%20Definitions.md). Production [notebooks](../Common%20Definitions.md), shared SQL, job code, and project documentation should live in a shared [GitHub](../Common%20Definitions.md)-backed project.

## Creating Git Folders

A [Git folder](../Common%20Definitions.md) is a Databricks [workspace](../Common%20Definitions.md) folder that is specifically connected to a [GitHub](../Common%20Definitions.md) repository. We will create our [git folders](../Common%20Definitions.md) in the shared location on the [workspace](../Common%20Definitions.md) so all users can access the folder and make changes to the repo. Note that a [Git folder](../Common%20Definitions.md) only needs to be created once.

Within the [workspace](../Common%20Definitions.md) navigate to the `shared` folder and select create then select [Git folder](../Common%20Definitions.md).

<img src="../images/git folder.PNG" alt="Create Git folder dialog" width="1000">

Paste the [GitHub](../Common%20Definitions.md) repo url and select create [Git folder](../Common%20Definitions.md).

<img src="../images/create git folder.PNG" alt="Create Git folder dialog" width="1000">

## Branching In Databricks

Now that the [Git folder](../Common%20Definitions.md) has been created we can view the branch to the right of the repo name. Click on the branch to enter the git UI where we can change branch or create a new branch.

<img src="../images/select branch.PNG" alt="Create Git folder dialog" width="1000">

Similarly we can select the three elipses and select `Git...` to enter the same git UI.

<img src="../images/enter git for changes.PNG" alt="Create Git folder dialog" width="1000">

## Committing In Databricks

After editing [notebooks](../Common%20Definitions.md), SQL files, or supporting project files in the Databricks [Git folder](../Common%20Definitions.md), enter the Git UI by using either method mentioned in the branching section. Review the changed files before committing. Commit only the files that belong to the current change.

<img src="../images/commit example.PNG" alt="Create Git folder dialog" width="1000">

## Pushing From Databricks

After committing, A push can be made from the same Git UI. A commit that has not been pushed is still only available from the Databricks [Git folder](../Common%20Definitions.md) where it was created.

## Pulling Into Databricks

Before starting new work in a shared [Git folder](../Common%20Definitions.md), pull the latest changes in Databricks. Pull again before committing if other team members may have updated the same project.

If Databricks reports a conflict during pull, stop and review the conflicting files before continuing. Do not overwrite another team member's work unless the team has agreed that the change should be replaced.
