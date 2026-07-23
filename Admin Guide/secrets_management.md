# Databricks Secret Management
[Back to Table of Contents](../README.md#table-of-contents)

Credentials - database passwords, API tokens, wallet passwords - must never be hardcoded in a notebook or committed to GitHub. Databricks Secrets store these values encrypted and expose them to code at runtime without ever printing them in plain text.

**Compute**: Works on all compute types (Serverless, job clusters, all-purpose). No special setup required beyond the Databricks CLI for creating secrets.

## Why Not Environment Variables or Hardcoding

| Approach | Problem |
|---|---|
| Hardcoded string in notebook | Visible to anyone with read access; leaks into GitHub on commit |
| Databricks Secrets | Encrypted at rest, access-controlled per scope, auto-redacted from notebook output |

Our current `db_config.py` reads Oracle credentials from `os.environ.get(...)`.
## Concepts

- **Secret scope** - a named container for a group of secrets (e.g., `oracle`, `sharepoint`)
- **Secret** - a single key-value pair inside a scope (e.g., key `password_prod`)
- **Backend** - where the scope is stored:
  - **Databricks-backed** - stored in the Databricks control plane. Simplest option.
  - **Azure Key Vault-backed** - the scope maps to an Azure Key Vault. Use when the org already manages secrets centrally in Key Vault.

## Creating Secrets

Secrets are created with the Databricks CLI or the REST API — not in a notebook (so the value never lands in notebook history).



### Create a scope

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
w.secrets.create_scope(scope="oao_secrets")
```

If scope already exists, use a different name for scope


### Listing Scopes
```python
# List all secret scopes in the workspace
for scope in w.secrets.list_scopes():
    print(f"Scope: {scope.name}, Backend: {scope.backend_type}")
```

### Set parameters - USERNAME/PASSWORD - Add secrets to the scope

```python
w.secrets.put_secret("oao_secrets","OAO_PRODUCTION",string_value ="<password>")
w.secrets.put_secret("oao_secrets","OAO_DEVELOPMENT",string_value ="<password>")
w.secrets.put_secret("oao_secrets","ORACLE_JDBC_URL",string_value ="<URL>")
```


## Reading Secrets in a Notebook

```python
secret_value = dbutils.secrets.get(scope="oao_secrets", key="OAO_PRODUCTION")
```

### Automatic redaction

Databricks redacts secret values from all notebook output. If you try to print one, you get `[REDACTED]`:

```python
print(secret_value)   # -> [REDACTED]
```

Redaction is literal — it masks the exact secret string wherever it appears in output. It does **not** protect against writing a secret to a file or an external API on purpose. Never do that.



This keeps `dbutils` in the notebook (where it exists) and leaves `db_config.py` free of any hardcoded or environment-based credentials.

## Access Control (Secret ACLs)

Scopes have permissions so only the right people and jobs can read a secret.

| Permission | Allows |
|---|---|
| `READ` | Read secret values and list keys in the scope |
| `WRITE` | Create and delete secrets in the scope |
| `MANAGE` | Change permissions on the scope |

Grant read access to a group:

```python
rom databricks.sdk.service.workspace import AclPermission

# Grant READ access (can retrieve secrets, cannot modify)
w.secrets.put_acl(scope="oao_secrets", principal="gregory.lenane@mssm.edu", permission=AclPermission.READ)

# Grant WRITE access (can read + add/delete secrets)
# w.secrets.put_acl(scope="oao_secrets", principal="some-group", permission=AclPermission.WRITE)

# Grant MANAGE access (full control including ACL changes)
w.secrets.put_acl(scope="oao_secrets", principal="gregory.lenane@mssm.edu", permission=AclPermission.MANAGE)

# List current ACLs on the scope
for acl in w.secrets.list_acls(scope="oao_secrets"):
    print(f"{acl.principal}: {acl.permission}")

# Remove an ACL
# w.secrets.delete_acl(scope="oao_secrets", principal="user@mssm.edu")```
```

List who has access:

```python
for acl in w.secrets.list_acls(scope="oao_secrets"):
    print(f"{acl.principal}: {acl.permission}")
```

For production jobs, grant `READ` to the service principal that runs the job — not to individual users. See [Job Scheduling](../Common%20Definitions.md#Databricks Terms) for the service-principal convention.

## Best Practices

- One scope per system or data domain (`oracle`, `sharepoint`, `azure_storage`) - not one giant scope
- Name keys by environment and role: `username_prod`, `password_dev`, `wallet_password`
- Never `print()`, log, or write a secret to a table, file, or external request
- Rotate secrets when a team member leaves or a token is suspected compromised - `put-secret` with the same key overwrites the old value
- Prefer a service principal (not a personal PAT) for the token behind production secret reads
- Store the Oracle wallet in a Volume, and its wallet password as a secret - never commit the wallet or its password

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| `RESOURCE_DOES_NOT_EXIST: Secret scope 'x' does not exist` | Scope not created, or typo | `databricks secrets list-scopes` to verify the name |
| `PERMISSION_DENIED` on `secrets.get` | Caller lacks `READ` on the scope | Grant `READ` via `put-acl` to the user or service principal |
| Value prints as `[REDACTED]` | Expected - redaction is working | Not an error; use the value in code, don't print it |
| `dbutils is not defined` in `db_config.py` | `dbutils` only exists in a notebook | Read the secret in the notebook and pass it into the function |
