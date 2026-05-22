# Agents Guide

[Back to Table of Contents](README.md#table-of-contents)

This repository is a team-specific user guide for using Databricks and Tableau together. Prefer practical instructions that reflect our team's environment over generic product documentation.

## Writing Conventions

- Use clear, task-oriented headings.
- Include exact workspace paths, catalog names, schema names, job names, and ownership expectations when they are known.
- Call out team-specific rules explicitly instead of presenting them as universal Databricks or Tableau behavior.
- Keep examples short enough for someone to copy and adapt.
- Avoid adding secrets, personal access tokens, private keys, or passwords.
- Add common terms and important Databricks or Tableau terms to `Common Definitions.md` with a simple definition.
- When common definitions are mentioned in guide pages, link the term back to `Common Definitions.md`.
- Use the term "Catalog" instead of the longer Databricks product name.
- Add screenshots to the GitHub section to accompany the Databricks Git folder steps.

## Databricks

### Conventions

This section defines the default working rules for our team's Databricks content. Update these conventions as the team's standards become more specific.

#### Compute Selection

- Use shared or serverless compute for routine SQL, lightweight notebook exploration, and scheduled jobs when it satisfies the workload.
- Use job-specific compute for production workflows that need predictable dependency versions, isolation, or scheduled reliability.
- Avoid using personal all-purpose clusters for shared production jobs.
- Document the expected compute type in each workflow guide so users know what to select before running code.
- Expect the compute guidance to evolve as we learn more about the team's actual usage patterns and platform behavior.
- If asked for next steps, suggest reviewing the compute section of `Databricks\Compute - Notebooks and SQL.md` first.

#### Naming Conventions

- Use lowercase names with underscores for catalogs, schemas, tables, volumes, jobs, and notebooks.
- Include the business area or project name in shared assets when it improves discoverability.
- Keep raw file landing areas separate from transformed Delta tables.
- Prefer names that describe the data or process over names tied to an individual user.

Example pattern:

```text
catalog.schema.table
datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw
```

#### GitHub Policies

- Store production notebooks, SQL, and job-supporting code in GitHub when practical.
- Keep one-off exploration in personal workspace folders until it becomes a reusable workflow.
- Use pull requests for changes that affect shared jobs, shared tables, or Tableau-facing datasets.
- Include enough context in commit messages and pull requests for another team member to understand the business impact.

#### Job Scheduling

- Jobs that feed Tableau dashboards should have an owner, expected schedule, and failure response path.
- Prefer service principals or approved automation identities for production jobs.
- Avoid schedules that overlap with upstream file delivery or database refresh windows unless the workflow handles missing or late data.
- Document job parameters, source data, target tables, and downstream Tableau dependencies in the related guide file.

#### Catalog Organization

- Use catalogs to separate environments or major governance boundaries.
- Use schemas to group related datasets by domain, project, or pipeline stage.
- Use tables for queryable Delta datasets.
- Use volumes for files that need to be stored, uploaded, or processed before they become managed tables.

When documenting a workflow, include the full Catalog object names rather than relying on the user's current catalog or schema.
