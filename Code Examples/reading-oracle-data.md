# Reading Oracle Data in Databricks

This guide covers how to connect a DatabricksNotebook to an Oracle database and read data into a Spark DataFrame.

**Compute**: Use OAO_DEVELOPMENT Compute or OAO_PRODUCTION Compute

## Prerequisites

- [Oracle Cloud Wallet](../../Common%20Definitions.md#oracle-cloud-wallet) (`.zip`) extracted and placed on the Databricks cluster (see [Wallet Extraction](../../Admin%20Guide/oracle-cloud-wallet/wallet-extraction.md))
- [DSN](../../Common%20Definitions.md#dsn-data-source-name) configured via ODBC Data Source Administrator (see [DSN Configuration](../../Admin%20Guide/oracle-cloud-wallet/dsn-configuration.md))
- `cx_Oracle` or `oracledb` Python library available on the cluster


### Connect and query

```python
import oracledb
import pandas as pd
import sys

sys.path.append("/Volumes/opsanalytics_adb_workspace01/default/oracle_connections")
from db_config import get_connection



# Thick mode required for wallet-based mTLS connections
conn = get_connection("production")
cursor = conn.cursor()
cursor.execute("SELECT 1 FROM DUAL")
print(cursor.fetchall())

# Parameters
sched_start_date = "2024-01-01"
sched_end_date = "2024-12-31"
status = "Completed"
room_exclusion_list = "('MSW OR 23','MSM OR 08','MSM OR 15')" # replace with your actual exclusions

# Table names
encounter_data_table_name = "MS_INSIGHT.OR_QUALITY_DASHBOARD_CASE_DETAILS"
room_master_data_table_name = "MS_INSIGHT.OR_QUALITY_DASHBOARD_ROOM_MASTER"
utlization_calculation_table = "MS_INSIGHT.OR_QUALITY_ROOM_UTIL_V"

query = f"""
    SELECT ENCOUNTERS.OR_CASE_ID,
           ENCOUNTERS.ENCOUNTER_NO_SRC,
           ENCOUNTERS.ENCOUNTER_ID,
           ENCOUNTERS.PAYOR_GROUP_DESC_MSX_OP,
           ENCOUNTERS.CCM_PAYOR_DESC_MSX_OP,
           ENCOUNTERS.PAYOR_GROUP_OP,
           ENCOUNTERS.CLINIC_GROUP_DESC_MSX,
           ENCOUNTERS.REG_AREA_DESC_SRC,
           ENCOUNTERS.ATTENDING_MD_NAME_MSX AS ATTENDING_MD,
           ENCOUNTERS.ATTENDING_MD_SPEC_SRC AS ATTENDING_MD_SPECIALIZATION,
           ENCOUNTERS.PRIMARY_SURGEON,
           ENCOUNTERS.SURGEON_SPECIALTY AS PRIMARY_SURGEON_SPECIALTY,
           ENCOUNTERS.PAT_CLASS_NAME AS PATIENT_CLASS,
           ENCOUNTERS.PAT_MRN_ID AS PATIENT_MRN,
           TO_CHAR(ENCOUNTERS.PAT_DOB,'YYYY-MM-DD') AS PATIENT_DOB,
           ENCOUNTERS.ADMIT_CSN_ID,
           ENCOUNTERS.TOTAL_TIME_NEEDED,
           ENCOUNTERS.PRIMARY_PROC_CODE AS PRIMARY_PROCEDURE_CODE,
           ENCOUNTERS.PRIMARY_PROCEDURE AS PRIMARY_PROCEDURE_DESC,
           ENCOUNTERS.ANESTHESIA_TYPE,
           ENCOUNTERS.SCHED_IN_ROOM_DTTM,
           ENCOUNTERS.SCHED_START_TIME,
           ENCOUNTERS.PATIENT_IN_ROOM_DTTM,
           ENCOUNTERS.PATIENT_OUT_ROOM_DTTM,
           ENCOUNTERS.MINUTES_IN_ROOM_TO_OUT_ROOM,
           ENCOUNTERS.TURNOVER_FROM_PRIOR_CASE,
           ENCOUNTERS.SURGERY_DATE,
           ROOM_MASTER.ROOM_ID,
           ROOM_MASTER.LOCATION_NM AS LOCATION_NAME,
           ROOM_MASTER.CLUSTER_NAME,
           ROOM_MASTER.ROOM_NM AS ROOM_NAME,
           ENCOUNTERS.ROBOTIC_SURGERY_DAVINCI_YN
    FROM {encounter_data_table_name} ENCOUNTERS
    LEFT JOIN {room_master_data_table_name} ROOM_MASTER 
        ON ENCOUNTERS.OR_ID = ROOM_MASTER.ROOM_ID
    LEFT JOIN {utlization_calculation_table} TEMPLATE_TIME 
        ON ENCOUNTERS.OR_CASE_ID = TEMPLATE_TIME.LOG_ID
    WHERE ENCOUNTERS.SURGERY_DATE >= TO_DATE('{sched_start_date}','YYYY-MM-DD')
      AND ENCOUNTERS.SURGERY_DATE <= TO_DATE('{sched_end_date}','YYYY-MM-DD')
      AND TEMPLATE_TIME.WEEKEND_YN = 'N'
      AND TEMPLATE_TIME.HOLIDAY_YN = 'N'
      AND ENCOUNTERS.CASE_STATUS = '{status}'
      AND ROOM_MASTER.ROOM_NM NOT IN {room_exclusion_list}
"""

cursor = conn.cursor()
cursor.execute(query)

columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(cursor.fetchall(), columns=columns)

print(f"Rows returned: {len(df)}")
print(df.head())
```
__Output :__
![Oracle Connection Test](../../images/OracleDatabricks.PNG)

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| `ORA-12541: TNS:no listener` | Wrong host or port in JDBC URL | Check the TNS entry in `tnsnames.ora` |
| `ORA-01017: invalid username/password` | Wrong credentials | Verify secrets, check for trailing whitespace |
| `SSL handshake failed` | Wallet path wrong or wallet not extracted | Confirm wallet files are at the path referenced in JDBC URL |
| `ClassNotFoundException: oracle.jdbc.OracleDriver` | JDBC jar not on cluster | Attach Oracle JDBC JAR to the cluster library |

## Notes:
- [`db_config`](../../Admin%20Guide/oracle-cloud-wallet/db_config.py) is python function specific to our team
- It facilitates connections to both `OAO_PRODUCTION` and `OAO_DEVELOPMENT`
