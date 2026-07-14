# Naming Conventions

[Back to Table of Contents](../README.md#table-of-contents)

Use names that describe the project and the data, not the person who created them.

## Schemas

Name each [schema](../Common%20Definitions.md#databricks-terms) with the project name. Keep the [schema](../Common%20Definitions.md#databricks-terms) name short, lowercase, and easy to understand at a glance. Always use `snake_case`.

Example:

```text
inpatient_capacity
lab
balanced_scorecards
```

## Tables And Volumes

Use `snake_case` for [tables](../Common%20Definitions.md#databricks-terms) and [volumes](../Common%20Definitions.md#databricks-terms). Keep names lowercase and separate words with underscores.

Examples:

```text
customer_summary
daily_sales_extract
incoming_csv_files
model_output_files
```

## Team Rule

- [Schema](../Common%20Definitions.md#databricks-terms) names identify the project.
- [Schema](../Common%20Definitions.md#databricks-terms), [table](../Common%20Definitions.md#databricks-terms), and [volume](../Common%20Definitions.md#databricks-terms) names use `snake_case`.
