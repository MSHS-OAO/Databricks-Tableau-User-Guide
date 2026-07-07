# DBT

[Back to Table of Contents](../README.md#table-of-contents)

[dbt](../Common%20Definitions.md#dbt-terms) is the framework our team uses for SQL transformations after source data has landed in the [Catalog](../Common%20Definitions.md#databricks-terms). In the standard ETL pattern, notebooks or other ingestion tasks load the raw source data first, then the Databricks job runs a dbt task to build the final tables or views used by Tableau and downstream analysis.

Use the [Oncology dbt project](https://github.com/MSHS-OAO/Oncology/tree/staging/oncology_dbt) as the current team reference implementation.

## Team Workflow

1. Land source data in the correct [Catalog](../Common%20Definitions.md#databricks-terms) and [schema](../Common%20Definitions.md#databricks-terms) before dbt runs.
2. Define those landed tables as dbt [sources](../Common%20Definitions.md#dbt-terms) in `models/schema.yml`.
3. Build transformations as SQL [models](../Common%20Definitions.md#dbt-terms) in the project `models` folder.
4. Add model and column tests in `models/schema.yml`.
5. Schedule the dbt task after the upstream notebook tasks in the Databricks [job](../Common%20Definitions.md#databricks-terms).

See [Job Scheduling](../Databricks/Job%20Scheduling.md) for the Databricks job task setup. The current team standard is to run `dbt deps` and then `dbt build`.

## Project Setup

Admins will have 4 requirements before a project can be configured with dbt
1. Download and install VScode
2. Download and install python
3. pip install dbt-databricks
4. Set up 3 schemas within opsanalytics_adb_workspace01
    1. project schema: for all static mapping/data files
    2. project_staging: for all local and staging runs
    3. for all production data used for reporting

Within the git repo opened in VScode:
1. run `dbt init` and select databricks
2. input the host from the serverless sql warehouse connection details page
3. enter the HTTP Path from the same page
4. enter schema as project_staging
5. enter catalog as opsanalytics_adb_workspace01
6. select personal access token and reach out to admins to receive token secret

Check your profiles.yml located at `C:\Users\username\.dbt\profiles.yml` appears like the below profile (note that the token has ben removed):

```yaml
oncology_dbt:
  outputs:
    dev:
      catalog: opsanalytics_adb_workspace01
      host: adb-7405606624435497.17.azuredatabricks.net
      http_path: /sql/1.0/warehouses/8f40c0f5ed465bfa
      schema: oncology_staging
      threads: 4
      token: REMOVED_FOR_SECURITY
      type: databricks
  target: dev
```
This is the profile used for local development so that you can run dbt models locally against the staging schema of your project. After navigating to the dbt folder within the repo, you can run `dbt debug` to test the connection
### GitHub Configuration

We will use deliberate branching structures, branch rules and github workflows to maintain CI/CD and to ensure we always develop on a staging schema before pushing updates to our production branches. 

In github make sure the repo has a staging and main branch. The staging branch will be used for all local and staging dbt runs. The production branch will be used for the production dbt run

#### Rulesets
1. within the github repo navigate to settings and select rules then rulesets
2. Create new ruleset and select new branch ruleset
    1. One ruleset will be made for main and one for staging. 
3. for the ruleset name enter staging or main as needed
4. for the branch targeting criteria add default branch for main and for staging include by pattern "staging"
5. Add branch rules:
    1. for staging check Restrict deletions, Require a pull request before merging and Block force pushes
    2. for main check Restrict deletions, Require deployments to succeed, Require a pull request before merging and Block force pushes
6. Make sure both rulesets are active

#### GitHub Workflows

We will use github workflows to ensure CI/CD best practices. This will ensure that as soon as we make updates to our DBT models, github will trigger a databricks job run so that the updated models are automatically reflected in databricks. 

1. First we need to create a staging and production environment in our repo to store variables and secrets used by their respective workflows
2. Navigate to settings > environments > New environment
    1. Create 1 environment named production and 1 named staging.
    2. Add the following variables to both environments:
        1. DATABRICKS_CLIENT_ID = `cd6f07ea-b52e-48ec-b2e9-1554b6cf4bc8`
        2. DATABRICKS_HOST = `https://adb-7405606624435497.17.azuredatabricks.net`
        3. DATABRICKS_JOB_ID = unique databricks job ID
3. Within databricks create two service principals by navigating to settings > identity and access > service principals
    1. Create two service principals that are databricks managed. Name them project-github-staging and project-github-production respectively. Leave default entitlements
    2. once the principals have been created generate a secret for both principals within the secrets submenu of the principal. Set lifetime to max 730 days. Token will generate, make sure you do not leave that screen until completing the next step.
    3. Within the appropriate github environment (staging/production) add a secret called DATABRICKS_CLIENT_SECRET = `databricks principle token`
4. Navigate to both the staging and production jobs for this project. Under prmissions, add the appropriate service principal to the job permissions with Can Manage Run permissions
5. Now we need to create github workflows which will essentially run the production and staging databricks job automatically any time a push is made to the main and staging branches respectively
6. Create a folder at the root of the github repo named `.github/workflows/`
7. Crate two files within this folder named `run-production.yml` and `run-staging.yml`
    1. Refer to [Oncology Workflows](https://github.com/MSHS-OAO/Oncology/tree/staging/.github/workflows) for example github workflows. Mimic the structure unless otherwise needed and only change the naming of items where appropriate.

## Development Guidelines

For additional dbt resources please visit [DBT Documentation](https://docs.getdbt.com/docs/introduction?version=2.0). For live examples refer to these two youtube resources:
1. [DBT with Databricks](https://www.youtube.com/watch?v=uRSLG63UR4w)
2. [DBT in depth Review](https://youtube.com/playlist?list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT&si=YSADXqSoKV77BMpJ)

<u>**Team Guidelines**</u>: It is critical to follow all steps in Project Setup for a successful project. Once the project has been set up and initialized it will be time to develop the necessary models and tests. It is important to branch off of staging for development since under this setup, you will not be able to commit to staging or main directly - you will have to merge into them. This way we can develop and test locally on a separate branch and push to staging/production only when we are ready. Refer to the documentation below for high level information and the above resources for a more in depth review of DBT. 

## DBT Folder Structure
The Oncology project keeps the dbt project in a dedicated repo folder:

```text
oncology_dbt/
  dbt_project.yml
  analyses/
  macros/
  models/
    mapping_active_mrn.sql
    mapping_ethnic_background.sql
    oncology_access_bronze.sql
    oncology_access_silver.sql
    oncology_access_gold.sql
    schema.yml
  seeds/
  snapshots/
  tests/
```

For new projects, use this same shape unless there is a clear reason to split the models into subfolders. Keep the dbt project folder name aligned to the business area or project, using lowercase names with underscores.

## dbt Project Configuration

The Oncology project's `dbt_project.yml` defines the project name, where dbt should look for files, and the default model behavior:

```yaml
name: 'oncology_dbt'
version: '1.0.0'
profile: 'oncology_dbt'

model-paths: ["models"]
analysis-paths: ["analyses"]
test-paths: ["tests"]
seed-paths: ["seeds"]
macro-paths: ["macros"]
snapshot-paths: ["snapshots"]

clean-targets:
  - "target"
  - "dbt_packages"

models:
  oncology_dbt:
    +materialized: view

vars:
  oncology_access_start_date: '2019-01-01'
  oncology_access_provider_name_regex: '\\[(.*?)\\]'
```

Team conventions from this setup:

- Set `+materialized: view` as the default for the project.
- Use model-level `config(materialized='table')` only when the model should be stored as a table.
- Store project variables in `dbt_project.yml` when the value is reused or should be easy to update between runs.
- Keep generated folders such as `target` and `dbt_packages` out of committed work.

## Sources

Define source tables in `models/schema.yml`. The Oncology project uses two source groups:

```yaml
sources:
  - name: oncology
    description: 'source for all OAO owned tables'
    database: opsanalytics_adb_workspace01
    schema: oncology

  - name: msx_clarity
    description: 'source for all MSX Clarity tables owned by DTP'
    database: datahub_dev_bronze
    schema: datahub_clarity
```

Use full Catalog object references in source definitions. Do not rely on a user's active Catalog or schema in the SQL editor.

Reference sources in models with `source()`:

```sql
with patient_data as (
    select *
    from {{ source('msx_clarity', 'mv_dm_patient_access') }}
)
```

## Model Pattern

The Oncology project uses short SQL models with common table expressions and a final `select * from final`. Follow that pattern because it makes the transformation steps easier to review in pull requests.

Use the bronze, silver, and gold naming pattern when it fits the workflow:

- `oncology_access_bronze.sql`: joins source and mapping data while keeping the raw grain and only the needed columns.
- `oncology_access_silver.sql`: formats columns, applies date filters, renames fields, and deduplicates rows.
- `oncology_access_gold.sql`: applies final business inclusion rules and materializes the Tableau-facing table.

Use mapping models for reusable lookup logic:

- `mapping_ethnic_background.sql` builds a patient-level ethnic background mapping from raw Clarity source tables.
- `mapping_active_mrn.sql` identifies active MRNs from the silver model and materializes the result as a table.

Reference other models with `ref()`:

```sql
with access_base as (
    select *
    from {{ ref('oncology_access_silver') }}
)
```

## Materialization Rules

The project default is [view materialization](../Common%20Definitions.md#dbt-terms). In Oncology, the final Tableau-facing model and selected mapping models are configured as tables:

```sql
{{ config(materialized='table') }}
```

Use views for intermediate logic unless performance, Tableau usage, or downstream dependency needs a table. If a model feeds Tableau directly or is expensive to recompute, consider table materialization and document why in the model description.

## Tests and Documentation

Keep model descriptions and tests in `models/schema.yml`. The Oncology project uses:

- Source table descriptions so reviewers know what each upstream table represents.
- Model descriptions that state the model grain or business purpose.
- `unique` tests on mapping keys such as `department_id`, `epic_provider_id`, and `pat_id`.
- `unique` and `not_null` tests on final encounter keys such as `pat_enc_csn_id`.
- Expression-based uniqueness tests for case-insensitive mapping values, such as `lower(race)`.

Example:

```yaml
models:
  - name: oncology_access_gold
    description: 'Final oncology access table downstream of oncology_access_silver with active MRN mapping and department/provider inclusion rules.'
    columns:
      - name: pat_enc_csn_id
        description: 'Unique appointment encounter identifier defining the grain of this model.'
        data_tests:
          - unique
          - not_null
```

Add tests when a column defines the grain, joins to mapping logic, or would break Tableau reporting if duplicated or missing.