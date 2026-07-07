# Job Notifications

[Back to Table of Contents](../README.md#table-of-contents)

Job notifications are an easy way for us to monitor jobs runs from outside of databricks. Using teams we can set alerts so that project teams can monitor their ETL runs automatically

## Setting Up Teams Webhook
<u>**Team Guidelines**</u>: One channel and webhook will be created for all staging and production notebooks. 

1. First the project will need a channel in the Databricks Job Log Team
2. Select the 3 dots next to the channel name and select workflows
3. Search for webhook and select the template for "Send webhook alerts to a channel"
4. Make sure the proper Team and Channel are selected and hit save

## Linking Teams Webhook to Job
1. Within the job UI navigate on the right hand pane to the job notification section
2. Select Edit notifications and select Add notification
3. If the notification has already been created in databricks, then select that destination. Otherwise select add new system destination which will redirect you
    1. Select manage next to notification destinations
    2. Select Add destination
    3. Select Microsoft Teams as destination
    4. Name it as project-job-log
    5. paste the Teams webhook url in the Microsoft Teams Webhook URL box
    6. select Create
    7. Navigate back to the notifiaction section of the job and select this newly created notification
4. check the success and failure boxes and hit save