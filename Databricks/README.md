## Oracle/Posit - Current State
```mermaid
flowchart LR
    subgraph Sources["Data Sources"]
        EPIC[Epic/MSX Clarity Extracts]
        ORA[("Oracle ADW<br>(internal refresh procs and views)")]
        EMAIL[Data Dumps via Email/Sharepoint/One Drive]
        XLS[Excel / CSV Inputs in Shared Drive]
    end
    subgraph DevOps["Development"]
        RS[POSIT Workbench]
        GH[GitHub Repos]
    end
    subgraph Deploy["POSIT Connect"]
        SHINY[Shiny Apps]
        RPT[Scheduled R Markdown Reports]
    end
    subgraph Users["End Users"]
        USR[Ops Leadership / Stakeholders]
    end

    EPIC --> ORA
    EMAIL -->|manual| XLS
    ORA <-->|CRUD| SHINY
    ORA <-->|CRUD| RPT
    ORA <-->|CRUD| RS
    XLS --> SHINY
    XLS <--> RPT
    XLS <--> RS
    RS <-->|develop / version control| GH
    GH -->|version control / deploy| SHINY
    GH -->|version control / deploy| RPT
    SHINY -->|real-time visualization| USR
    RPT -->|snapshot visualization| USR
    USR -->|real-time inputs| SHINY

    classDef navy fill:#212070,stroke:#212070,color:#ffffff
    classDef animate stroke-dasharray: 9,5,stroke-dashoffset: 900,animation: dash 25s linear infinite
    classDef cyan fill:#06ABEB,stroke:#0689BC,color:#ffffff
    classDef magenta fill:#DC298D,stroke:#B02171,color:#ffffff
    classDef gray fill:#63666A,stroke:#63666A,color:#ffffff
    class EPIC,ORA,EMAIL,XLS navy
    class RS,GH cyan
    class SHINY,RPT magenta
    class e1 animate
    class USR gray
```
Note:
- CRUD : Create, Read, Update and Delete
- internal refresh procs and views : Oracle provided abilities through `Oracle Procedures Module` to create a job and run based on specified cadence to refresh tables 

## Databricks/Tableau/Power Automate - Transitional State
```mermaid
flowchart LR
    subgraph Sources["Data Sources"]
        EPIC[Epic/MSX Clarity Extracts]
        ORA[("Oracle ADW<br>(internal refresh procs and views)")]
        EMAIL[Data Dumps via Email/Sharepoint/One Drive]
    end
    subgraph DBX["Databricks"]
        VOL[Unity Catalog Volumes]
        JOBS[Python Notebooks / Scheduled Jobs]
        DLT[Delta Tables<br>Bronze / Silver / Gold]
    end
    subgraph DevOps["Development"]
        GH[GitHub Repos]
    end
    subgraph Viz["Visualization"]
        TAB[Tableau Dashboards]
    end
    subgraph Users["End Users"]
        USR[Ops Leadership / Stakeholders]
    end
    EPIC --> ORA
    EMAIL -->|Power Automate| VOL
    ORA <-->|CRUD| JOBS
    VOL <--> JOBS
    JOBS <-->|CRUD| DLT
    GH <-->|develop / version control / deploy| JOBS
    DLT -->|live or extract connection| TAB
    TAB --> USR
    USR --> EMAIL
  
    classDef navy fill:#212070,stroke:#212070,color:#ffffff
    classDef cyan fill:#06ABEB,stroke:#0689BC,color:#ffffff
    classDef magenta fill:#DC298D,stroke:#B02171,color:#ffffff
    classDef gray fill:#63666A,stroke:#63666A,color:#ffffff
    class EPIC,ORA,EMAIL navy
    class GH cyan
    class VOL,DLT,JOBS,TAB magenta
    class USR,INP gray
```
Note:
- CRUD : Create, Read, Update and Delete
## Databricks/Tableau/Power Automate - Future State
```mermaid
flowchart LR
    subgraph Sources["Data Sources"]
        EPIC[Epic/MSX Clarity Extracts]
        EMAIL[Data Dumps via Email/Sharepoint/One Drive]
    end
    subgraph DBX["Databricks"]
        VOL[Unity Catalog Volumes]
        JOBS[Python Notebooks / Scheduled Jobs]
        DLT[Delta Tables<br>Bronze / Silver / Gold]
    end
    subgraph DevOps["Development"]
        GH[GitHub Repos]
    end
    subgraph Viz["Visualization"]
        TAB[Tableau Dashboards]
    end
    subgraph Users["End Users"]
        USR[Ops Leadership / Stakeholders]
    end
    EPIC -->DLT
    EMAIL -->|Power Automate| VOL
    VOL <--> JOBS
    JOBS <-->|CRUD| DLT
    GH <-->|develop / version control / deploy| JOBS
    DLT -->|live or extract connection| TAB
    TAB --> USR
    USR --> EMAIL
  
    classDef navy fill:#212070,stroke:#212070,color:#ffffff
    classDef cyan fill:#06ABEB,stroke:#0689BC,color:#ffffff
    classDef magenta fill:#DC298D,stroke:#B02171,color:#ffffff
    classDef gray fill:#63666A,stroke:#63666A,color:#ffffff
    class EPIC,ORA,EMAIL navy
    class GH cyan
    class VOL,DLT,JOBS,TAB magenta
    class USR,INP gray
```
Note:
- CRUD : Create, Read, Update and Delete
