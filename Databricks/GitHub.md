# GitHub Conventions

[Git folders](../Common%20Definitions.md) will be used as the standard convention for version control of all project work. Personal workspace folders are fine for early exploration. You can create whatever folders/files in your personal location in the workspace. Production notebooks, shared SQL, job code, and project documentation should live in a shared GitHub-backed project.

## Creating Git Folders

A [Git folder](../Common%20Definitions.md) is a Databricks workspace folder that is specifically connected to a GitHub repository. We will create our git folders in the shared location on the workspace so all users can access the folder.

Within the workspace navigate to the `shared` folder and select create then select git folder.

<img src="../images/git folder.PNG" alt="Create Git folder dialog" width="1000">

Paste the github repo url and select create git folder.

<img src="../images/create git folder.PNG" alt="Create Git folder dialog" width="1000">

## Branching In Databricks

Now that the git folder has been created we can view the branch to the right of the repo name. Click on the branch to enter the git UI where we can change branch or create a new one.

<img src="../images/select branch.PNG" alt="Create Git folder dialog" width="1000">

Similarly we can select the three elipses and select `Git...` to enter the same git UI.

<img src="../images/enter git for changes.PNG" alt="Create Git folder dialog" width="1000">

## Committing In Databricks

After editing notebooks, SQL files, or supporting project files in the Databricks Git folder, enter the Git UI by using method mentioned in the branching section to review the changed files before committing. Commit only the files that belong to the current change.

<img src="../images/commit example.PNG" alt="Create Git folder dialog" width="1000">

## Pushing From Databricks

After committing, A push can be made from the same Git UI. A commit that has not been pushed is still only available from the Databricks Git folder where it was created.

## Pulling Into Databricks

Before starting new work in a shared Git folder, pull the latest changes in Databricks. Pull again before committing if other team members may have updated the same project.

If Databricks reports a conflict during pull, stop and review the conflicting files before continuing. Do not overwrite another team member's work unless the team has agreed that the change should be replaced.
