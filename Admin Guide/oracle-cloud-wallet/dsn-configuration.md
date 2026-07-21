# DSN Configuration (Schemas)
[Back to Table of Contents](../../README.md#table-of-contents)

A **[DSN (Data Source Name)](../../Common%20Definitions.md#dsn-data-source-name)** is a named connection configuration that ODBC clients — including Tableau Desktop and Excel — use to connect to a database. For Oracle Autonomous Database, the DSN references the extracted [wallet](../../Common%20Definitions.md#oracle-cloud-wallet) and points to a specific schema (service name).


__Note:__
- Only needed for local database connections (Windows)
- You may not have access to `C:\` Drive, Raise ticket on service now portal or call DTP Help desk and ask for *`Developer Permisions on local laptop`*

## Prerequisites

- Oracle Instant Client installed (see below)
- Oracle Cloud Wallet extracted (see [Wallet Extraction](./wallet-extraction.md))
- Oracle ODBC driver installed

## Step 1: Install Oracle Instant Client

The Oracle Instant Client provides the libraries the ODBC driver needs.

1. Go to [Oracle's Instant Client download page](https://www.oracle.com/database/technologies/instant-client/downloads.html)
2. Download the **Basic Package** and the **ODBC Package** for your OS (e.g., Windows x64)
3. Extract both ZIPs to the same directory, e.g.:
   ```
   C:\oracle\instantclient_21_x\
   ```
4. Add that directory to your system `PATH` environment variable:
   - Search **Edit the system environment variables** in Windows
   - Click **Environment Variables → System variables → Path → Edit**
   - Add `C:\oracle\instantclient_21_x`
5. Run `odbc_install.exe` from the Instant Client directory to register the ODBC driver

## Step 2: Configure tnsnames.ora

The `tnsnames.ora` file inside your wallet defines connection aliases. Each alias maps to a service name (schema entry point). Open the file and verify the aliases:

```
<db_name>_high = (DESCRIPTION = (ADDRESS = (PROTOCOL = tcps)(PORT = 1522)
  (HOST = <adb_host>.oraclecloud.com))
  (CONNECT_DATA = (SERVER = dedicated)(SERVICE_NAME = <service>_high.adb.oraclecloud.com))
  (SECURITY = (SSL_SERVER_DN_MATCH = yes)))

<db_name>_medium = ...
<db_name>_low = ...
```

Common service tiers:
| Alias suffix | Use case |
|---|---|
| `_high` | High concurrency, managed parallelism |
| `_medium` | Balanced — use for most workloads |
| `_low` | Background / batch workloads |

## Step 3: Set TNS_ADMIN Environment Variable

`TNS_ADMIN` tells Oracle clients where to find `tnsnames.ora` and `sqlnet.ora`.

1. Open **System Environment Variables**
2. Add a new **system variable**:
   - Name: `TNS_ADMIN`
   - Value: `C:\oracle\wallet\<database_name>` (the folder containing your extracted wallet)
3. Restart any applications that need to pick up this variable (ODBC Data Source Administrator, Tableau Desktop)

## Step 4: Create the DSN

1. Search for **ODBC Data Sources (64-bit)** in the Windows Start menu and open it
2. Click the **System DSN** tab → **Add**
3. Select **Oracle in OraClient21Home1** (or the installed driver name) → **Finish**
4. Fill in the configuration:

| Field | Value |
|---|---|
| Data Source Name | A short, descriptive name (e.g., `OracleADB_Medium`) |
| Description | Optional note |
| TNS Service Name | One of the aliases from `tnsnames.ora` (e.g., `<db_name>_medium`) |
| User ID | Your Oracle database username |

5. Click **Test Connection** — enter your password when prompted
6. A dialog box should confirm **Connection successful**
7. Click **OK** to save

## Step 5: Connect from Tableau

1. Open Tableau Desktop
2. Click **Connect → To a Server → Other Databases (ODBC)**
3. In the DSN dropdown, select the DSN you created (e.g., `OracleADB_Medium`)
4. Enter your Oracle username and password
5. Click **Sign In**
6. Tableau will show the available schemas. Select a schema to browse tables.

## Multiple Schemas

Each schema in Oracle is typically a different user/service combination. To connect to a different schema:

- Either create a separate DSN pointing to the same TNS alias but logging in as a different Oracle user
- Or, inside Tableau, change the **Schema** dropdown after connecting — Tableau shows all schemas the connected user has `SELECT` access to

## Troubleshooting

### `ORA-12154: TNS:could not resolve the connect identifier`
`TNS_ADMIN` is not set, or points to a folder that doesn't contain `tnsnames.ora`. Verify the environment variable and restart the ODBC Administrator.

### `ORA-12560: TNS:protocol adapter error`
Oracle Instant Client is not on the `PATH`, or the ODBC driver was installed for a different architecture (32-bit vs 64-bit). Use ODBC Data Sources (64-bit) for 64-bit applications.

### `SSL handshake failed`
`sqlnet.ora` `WALLET_LOCATION` path doesn't match the actual extraction directory. Open `sqlnet.ora` and correct the path.

### `ORA-01017: invalid username/password; logon denied`
Wrong credentials. Oracle usernames are case-sensitive in some configurations — try uppercase.

### Test Connection button is greyed out
The ODBC driver is not installed or not visible to the ODBC Administrator. Re-run `odbc_install.exe` and reopen the Administrator.
