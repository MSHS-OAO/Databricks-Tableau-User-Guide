# Job Notifications

[Back to Table of Contents](../README.md#table-of-contents)

Job notifications are an easy way for us to monitor [job](../Common%20Definitions.md#databricks-terms) runs from outside of Databricks. Using Teams, we can set alerts so that project teams can monitor their ETL runs automatically.

## Setting Up Teams Webhook
<u>**Team Guidelines**</u>: One channel and [webhook](../Common%20Definitions.md#databricks-terms) will be created for all staging and production [notebooks](../Common%20Definitions.md#databricks-terms).

1. First the project will need a channel in the Databricks Job Log Team.
2. Select the 3 dots next to the channel name and select workflows.
3. Search for [webhook](../Common%20Definitions.md#databricks-terms) and select the template for "Send webhook alerts to a channel".
4. Make sure the proper Team and Channel are selected and hit save.

## Linking Teams Webhook to Job
1. Within the job UI, navigate on the right-hand pane to the job notification section.
2. Select Edit notifications and select Add notification.
3. If the notification has already been created in Databricks, then select that destination. Otherwise select add new system destination, which will redirect you.
    1. Select manage next to notification destinations.
    2. Select Add destination.
    3. Select Microsoft Teams as destination.
    4. Name it as project-job-log.
    5. Paste the Teams [webhook](../Common%20Definitions.md#databricks-terms) URL in the Microsoft Teams Webhook URL box.
    6. Select Create.
    7. Navigate back to the notification section of the job and select this newly created notification.
4. Check the success and failure boxes and hit save.
