# GitHub Policies

[Back to Table of Contents](../../README.md#table-of-contents)

Version control keeps our pipelines reproducible and gives the team visibility into what changed and why. These policies define when to use GitHub and how to collaborate on shared Databricks code.

## What Belongs in GitHub

| Asset | GitHub? | Notes |
|---|---|---|
| Production notebooks | ✅ Yes | Any notebook attached to a scheduled job |
| SQL scripts used by jobs or Tableau | ✅ Yes | |
| Job configuration files | ✅ Yes | |
| One-off exploration notebooks | ❌ No | Keep in personal workspace folder until promoted |
| Credentials, tokens, passwords | ❌ Never | Use Databricks Secrets or Azure Key Vault |
| Wallet files | ❌ Never | Binary credentials — store in a Volume |

## Connecting a Databricks Notebook to GitHub

1. In the Databricks sidebar, go to the notebook you want to version
2. Click **File → Git preferences** (or the branch icon in the top toolbar)
3. Connect your GitHub account if not already linked
4. Set the repository, branch, and file path
5. Click **Save** — the notebook is now tracked in the linked repo

Changes made to the notebook in Databricks can be committed and pushed from inside the notebook UI.

## Branch Strategy

- **`main`** — stable, production-ready code only
- **Feature branches** — use for new pipelines or significant changes (`feature/oracle-daily-sync`)
- **Fix branches** — use for targeted repairs (`fix/bsc-finance-schema-drift`)

Never push directly to `main`. Always work on a branch and open a pull request.

## Pull Request Requirements

Open a pull request for any change that affects:
- A shared production job
- A shared table or schema used by Tableau
- A notebook used by more than one person

PR description should answer:
- What does this change do?
- Which job, table, or dashboard is affected?
- How was it tested?

Keep PRs focused — one pipeline or one fix per PR. Large all-at-once changes are hard to review and harder to roll back.

## Commit Messages

Write commit messages that explain the business impact, not just the code change.

**Good**: `Add openpyxl install step to bsc_finance_ingest — fixes failure on serverless`
**Avoid**: `fixed notebook`, `update`, `changes`

A team member who wasn't in the original conversation should be able to understand why the commit exists just by reading the message.

## What to Do with Personal Notebooks

Keep exploratory work in `/Workspace/Users/name@mssm.edu/` until it is ready to become a shared workflow. Once promoted:
1. Move the notebook to `/Workspace/Shared/` or a project folder
2. Rename it using the [Naming Conventions](./naming-conventions.md)
3. Connect it to the team GitHub repo
4. Create a job to run it on schedule
