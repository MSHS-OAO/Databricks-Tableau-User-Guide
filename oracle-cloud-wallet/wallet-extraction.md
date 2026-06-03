# Oracle Cloud Wallet — Extraction

The [Oracle Cloud Wallet](../Common%20Definitions.md#oracle-cloud-wallet) is a ZIP archive that contains the SSL certificates, connection descriptors, and credential files needed to establish a secure mTLS connection from any client (Databricks, ODBC, JDBC) to an Oracle Autonomous Database.

## What's Inside the Wallet

| File | Purpose |
|---|---|
| `cwallet.sso` | Auto-login wallet (no password required at connect time) |
| `ewallet.p12` | PKCS#12 wallet (password-protected) |
| `tnsnames.ora` | Connection aliases and full TNS descriptors |
| `sqlnet.ora` | Oracle Net configuration, points to wallet directory |
| `ojdbc.properties` | JDBC-specific wallet configuration |
| `keystore.jks` | Java KeyStore (used by JDBC) |
| `truststore.jks` | Java TrustStore (used by JDBC) |


## Extracting the Wallet

The wallet must be extracted to a directory that is accessible to the connecting client.

### On Windows (for ODBC/Tableau connections)

1. Create a dedicated directory, e.g.:
   ```
   C:\oracle\wallet\<database_name>\
   ```
2. Right-click the downloaded ZIP → **Extract All**
3. Extract to the directory above
4. Verify the directory contains `tnsnames.ora` and `sqlnet.ora`

### On a Databricks Cluster (for notebook/job connections)

Upload the wallet files to a Databricks Volume or DBFS, then reference the path in connection code:

```python
# Example: wallet extracted to a Volume
wallet_dir = "/Volumes/datahub_dev_bronze/config/oracle_wallet"
```

Or use `dbutils.fs.cp` to copy from DBFS:

```python
import os
os.makedirs("/tmp/wallet", exist_ok=True)
dbutils.fs.cp("dbfs:/FileStore/oracle_wallet/", "file:/tmp/wallet/", recurse=True)
wallet_dir = "/tmp/wallet"
```

## Configuring sqlnet.ora

After extraction, update `sqlnet.ora` so `WALLET_LOCATION` points to the directory where you extracted the wallet. Open the file in a text editor:

```
WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="C:\oracle\wallet\<database_name>")))
SSL_SERVER_DN_MATCH=yes
```

Replace the path with the actual extraction directory. On Windows, use forward slashes or escape backslashes.

## Rotating the Wallet

Oracle Autonomous Database wallets have no built-in expiry, but should be rotated when:
- A team member with wallet access leaves
- You suspect the wallet has been compromised
- Oracle requires re-download after a maintenance event

To rotate:
1. Download a new wallet from the OCI console (same steps as above)
2. Replace the old wallet files in all locations (Databricks Volume, local ODBC path, etc.)
3. Update DSN configurations if the wallet path changed
4. Test connectivity before decommissioning the old wallet

## Security Notes

- Never commit wallet files to a git repository
- Store `ewallet.p12` password in a secrets manager (Databricks Secrets, Azure Key Vault)
- The `cwallet.sso` file grants passwordless access — restrict file system permissions accordingly
