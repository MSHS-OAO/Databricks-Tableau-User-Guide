# Common Definitions

Quick-reference definitions for terms used throughout this guide. Click any term for the full tutorial.

---

## Catalog

The top level of the three-level namespace `catalog.schema.table`. Catalogs separate environments or major governance boundaries. See [What is a Catalog?](common-definitions/what-is-catalog.md).

Example: `datahub_dev_bronze`

---

## Schema

The second level of the namespace, sitting inside a Catalog. Schemas group related datasets by domain, project, or pipeline stage.

Example: `datahub_dev_bronze.scorecards_raw_files`

---

## Table

A queryable Delta dataset stored inside a Schema. Use `SELECT` statements to read from it. Tables are the main output of ingestion pipelines and the primary input for Tableau.

Example: `datahub_dev_bronze.scorecards_raw_files.bsc_finance_raw`

---

## Volume

A Catalog object that stores raw files (Excel, CSV, JSON) before they are processed into managed tables. Volumes live inside a Schema and act as the file landing zone.

Example: `/Volumes/datahub_dev_bronze/scorecards_raw_files/finance/`

---

## Notebook

An interactive document in the Databricks Workspace where you write and run code in cells. Supports Python, SQL, Scala, and R. See [Notebook](common-definitions/notebook.md).

---

## SQL Query

A statement that reads or transforms data in a Delta table. In Databricks, SQL runs in the SQL Editor or inside a `%sql` notebook cell against Catalog tables. See [SQL Query](common-definitions/sql-query.md).

---

## Job

A Databricks Workflow that schedules and runs a notebook or script automatically — triggered by a schedule, an API call, or another system such as Power Automate. See [Job](common-definitions/job.md).

---

## Power Automate

A Microsoft 365 cloud automation platform that connects services without custom server code. Used to watch SharePoint, Outlook, and OneDrive for new files and forward them to Databricks via REST API. See [Power Automate](common-definitions/power-automate.md).

---

## Delta Table

The default table format in Databricks. Delta adds ACID transactions, schema enforcement, and time travel (version history) on top of Parquet files. All managed tables in our Catalog are Delta tables.

---

## REST API

A way for two systems to communicate over HTTP. Databricks exposes a REST API that lets external tools — including Power Automate — upload files, trigger jobs, and check run status by sending HTTP requests to a URL.

Each request includes:
- A **verb** (GET, POST, PUT, DELETE) that says what operation to perform
- A **URL** that identifies the resource (e.g., a specific job or file path)
- An **Authorization header** containing a [Personal Access Token](#personal-access-token-pat) to prove identity
- Optionally, a **body** with data to send (for POST and PUT requests)

See [HTTP Methods](common-definitions/power-automate.md#http-methods) for the full verb reference.

---

## Personal Access Token (PAT)

A credential string used to authenticate REST API calls to Databricks. Generated under **Settings → Developer → Access Tokens**. Scopes (`files`, `jobs`, `sql`) limit what the token can do. Never store a PAT in a notebook or commit it to git — use Databricks Secrets or Azure Key Vault.

---

## Databricks Secret

A key-value credential stored securely in a Databricks Secret Scope. Accessed in notebooks with `dbutils.secrets.get(scope="<scope>", key="<key>")`. Use secrets to keep passwords and tokens out of notebook code.

---

## Oracle Cloud Wallet

A ZIP archive containing SSL certificates and connection descriptors needed to establish a secure connection from Databricks or ODBC clients to Oracle Autonomous Database. See [Wallet Extraction](Admin%20Guide/oracle-cloud-wallet/wallet-extraction.md).

---

## DSN (Data Source Name)

A named connection profile in the Windows ODBC Data Source Administrator. Tableau Desktop and other ODBC clients use a DSN to connect to a database without specifying the full connection string each time. See [DSN Configuration](Admin%20Guide/oracle-cloud-wallet/dsn-configuration.md).

---

## Serverless Compute

A Databricks compute option with no cluster startup wait. Recommended for scheduled jobs, lightweight SQL, and notebook exploration. Costs nothing when idle. Use this as the default for new jobs unless the workload requires specific libraries or a fixed cluster configuration.
