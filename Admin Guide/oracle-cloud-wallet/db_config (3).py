import oracledb
import os
from databricks.sdk.runtime import dbutils

def get_connection(schema="development"):
    # path to wallet and setting connection
    wallet_dir = "/Volumes/opsanalytics_adb_workspace01/default/oracle_wallet"
    conn =  None

    if schema == "production": 
        conn = oracledb.connect(
            user="OAO_PRODUCTION",
            password=dbutils.secrets.get(scope="oao_secrets", key="OAO_PRODUCTION"),
            dsn="adwdbtst_low",
            config_dir=wallet_dir,
            wallet_location=wallet_dir,
            wallet_password=""
        )
    else:
        conn = oracledb.connect(
            user="OAO_DEVELOPMENT",
            password=dbutils.secrets.get(scope="oao_secrets", key="OAO_DEVELOPMENT"),
            dsn="adwdbtst_low",
            config_dir=wallet_dir,
            wallet_location=wallet_dir,
            wallet_password=""
        )          
    return conn
