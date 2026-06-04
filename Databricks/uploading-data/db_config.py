
import oracledb
import os

def get_connection(schema="development"):
    # path to wallet and setting connection
    wallet_dir = "/Volumes/opsanalytics_adb_workspace01/default/oracle_wallet"
    conn =  None

    if schema == "production": 
        conn = oracledb.connect(
            user=os.environ.get("ORACLE_PRODUCTION"),
            password=os.environ.get("ORACLE_PASSWORD_PROD"),
            dsn="adwdbtst_low",
            config_dir=wallet_dir,
            wallet_location=wallet_dir,
            wallet_password=""
        )
    else:
        conn = oracledb.connect(
            user=os.environ.get("ORACLE_DEVELOPMENT"),
            password=os.environ.get("ORACLE_PASSWORD_DEV"),
            dsn="adwdbtst_low",
            config_dir=wallet_dir,
            wallet_location=wallet_dir,
            wallet_password=""
        )          
    return conn
    
