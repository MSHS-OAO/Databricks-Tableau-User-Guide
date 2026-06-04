# Reading Oracle Data in Databricks

This guide covers how to connect a Databricks [Notebook](../../Common%20Definitions.md#notebook) to an Oracle database and read data into a Spark DataFrame.

**Compute**: Use [Serverless Compute](../../Common%20Definitions.md#serverless-compute) for exploratory reads. For scheduled ingestion jobs, attach a job-specific cluster with the Oracle JDBC JAR configured as a cluster library so dependency versions are fixed.

## Prerequisites

- [Oracle Cloud Wallet](../../Common%20Definitions.md#oracle-cloud-wallet) (`.zip`) extracted and placed on the Databricks cluster (see [Wallet Extraction](../../Admin%20Guide/oracle-cloud-wallet/wallet-extraction.md))
- [DSN](../../Common%20Definitions.md#dsn-data-source-name) configured via ODBC Data Source Administrator (see [DSN Configuration](../../Admin%20Guide/oracle-cloud-wallet/dsn-configuration.md))
- `cx_Oracle` or `oracledb` Python library available on the cluster

## Option 1: JDBC Connection (Recommended for Spark)

JDBC is the standard way to read from relational databases into Spark. It parallelizes reads across partitions.

### Step 1: Store credentials as Databricks Secrets

Never hardcode passwords in a notebook. Use Databricks Secrets:

```bash
# In Databricks CLI
databricks secrets create-scope --scope oracle
databricks secrets put --scope oracle --key username
databricks secrets put --scope oracle --key password
```

### Step 2: Read with JDBC

```python
username = dbutils.secrets.get(scope="oracle", key="username")
password = dbutils.secrets.get(scope="oracle", key="password")

jdbc_url = (
    "jdbc:oracle:thin:@(DESCRIPTION="
    "(ADDRESS=(PROTOCOL=tcps)(HOST=<oracle-host>)(PORT=1522))"
    "(CONNECT_DATA=(SERVICE_NAME=<service_name>))"
    "(SECURITY=(SSL_SERVER_DN_MATCH=yes)))"
)

df = (
    spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("dbtable", "SCHEMA_NAME.TABLE_NAME")
    .option("user", username)
    .option("password", password)
    .option("driver", "oracle.jdbc.OracleDriver")
    .load()
)

df.printSchema()
df.show(5)
```

### Step 3: Write to Catalog

```python
df.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable(
    "datahub_dev_bronze.oracle_raw.table_name"
)
```

## Option 2: cx_Oracle / python-oracledb

Use this approach when you need finer control or when the Oracle JDBC driver is unavailable.

### Install the library

```python
%pip install oracledb
dbutils.library.restartPython()
```

### Connect and query

```python
import oracledb
import pandas as pd

username = dbutils.secrets.get(scope="oracle", key="username")
password = dbutils.secrets.get(scope="oracle", key="password")

# Thick mode required for wallet-based mTLS connections
oracledb.init_oracle_client()

conn = oracledb.connect(
    user=username,
    password=password,
    dsn="<TNS_alias>",          # alias from tnsnames.ora in the wallet
    config_dir="/path/to/wallet",
    wallet_location="/path/to/wallet",
    wallet_password="<wallet_password>"
)

query = "SELECT * FROM SCHEMA_NAME.TABLE_NAME WHERE ROWNUM <= 1000"
pdf = pd.read_sql(query, conn)
conn.close()

df = spark.createDataFrame(pdf)
df.show(5)
```

## Partition Strategy for Large Tables

Reading a large Oracle table as a single JDBC partition is slow. Use `partitionColumn`, `lowerBound`, `upperBound`, and `numPartitions` to parallelize:

```python
df = (
    spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("dbtable", "SCHEMA_NAME.LARGE_TABLE")
    .option("user", username)
    .option("password", password)
    .option("driver", "oracle.jdbc.OracleDriver")
    .option("partitionColumn", "ROW_ID")
    .option("lowerBound", "1")
    .option("upperBound", "10000000")
    .option("numPartitions", "10")
    .load()
)
```

Each partition runs as a separate SQL query with a `WHERE ROW_ID BETWEEN ...` clause.

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| `ORA-12541: TNS:no listener` | Wrong host or port in JDBC URL | Check the TNS entry in `tnsnames.ora` |
| `ORA-01017: invalid username/password` | Wrong credentials | Verify secrets, check for trailing whitespace |
| `SSL handshake failed` | Wallet path wrong or wallet not extracted | Confirm wallet files are at the path referenced in JDBC URL |
| `ClassNotFoundException: oracle.jdbc.OracleDriver` | JDBC jar not on cluster | Attach Oracle JDBC JAR to the cluster library |
