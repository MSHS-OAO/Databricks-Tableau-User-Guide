# Reading Oracle Data in Databricks

This guide covers how to connect a Databricks [Notebook](../../Common%20Definitions.md#notebook) to an Oracle database and read data into a Spark DataFrame.

**Compute**: Use [Serverless Compute](../../Common%20Definitions.md#serverless-compute) for exploratory reads. For scheduled ingestion jobs, attach a job-specific cluster with the Oracle JDBC JAR configured as a cluster library so dependency versions are fixed.

## Prerequisites

- [Oracle Cloud Wallet](../../Common%20Definitions.md#oracle-cloud-wallet) (`.zip`) extracted and placed on the Databricks cluster (see [Wallet Extraction](../../Admin%20Guide/oracle-cloud-wallet/wallet-extraction.md))
- [DSN](../../Common%20Definitions.md#dsn-data-source-name) configured via ODBC Data Source Administrator (see [DSN Configuration](../../Admin%20Guide/oracle-cloud-wallet/dsn-configuration.md))
- `cx_Oracle` or `oracledb` Python library available on the cluster

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

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| `ORA-12541: TNS:no listener` | Wrong host or port in JDBC URL | Check the TNS entry in `tnsnames.ora` |
| `ORA-01017: invalid username/password` | Wrong credentials | Verify secrets, check for trailing whitespace |
| `SSL handshake failed` | Wallet path wrong or wallet not extracted | Confirm wallet files are at the path referenced in JDBC URL |
| `ClassNotFoundException: oracle.jdbc.OracleDriver` | JDBC jar not on cluster | Attach Oracle JDBC JAR to the cluster library |
