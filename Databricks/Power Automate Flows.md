
## Power Automate Flows

[Back to Table of Contents](../README.md#table-of-contents)

Every flow has three parts:

- **Trigger** — the event that starts the flow (a file is uploaded, an email arrives, a schedule fires)
- **Actions** — steps that execute in order after the trigger
- **Outputs** — data passed between steps via dynamic content

### Creating a Flow

1. Go to [make.powerautomate.com](https://make.powerautomate.com)
2. Click **Create → Automated cloud flow**
3. Search for your trigger (e.g., "SharePoint — When a file is created")
4. Add actions using the **+** button between steps

### HTTP Methods

HTTP verbs tell the server what operation to perform. Power Automate HTTP actions require you to pick the correct verb:

| Verb | Operation | Databricks Example |
|---|---|---|
| `GET` | Read / retrieve a resource | List jobs, check run status, download a file |
| `POST` | Create a new resource or trigger an action | Trigger a job run, create a cluster |
| `PUT` | Replace a resource at a specific path | Upload a file to a Volume (replaces if exists) |
| `PATCH` | Partially update an existing resource | Update a job's schedule |
| `DELETE` | Remove a resource | Delete a file from a Volume |


### Dynamic Content and Expressions

Power Automate passes data between steps using **dynamic content** (point-and-click) or **expressions** (typed in the `fx` bar).

Dynamic content inserts values from previous steps:
- `triggerOutputs()?['body/{FilenameWithExtension}']` — filename from a SharePoint trigger

Expressions transform values:
- `base64ToBinary(body('Get_file_content_using_path')?['$content'])` — decodes base64-encoded file content back to raw binary

Always enter expressions via the **fx** button in the action panel. Typing them as plain text sends the literal string instead of evaluating it.
![FX](./images/fx.PNG)

### Testing a Flow

Use **Test** (top right of the flow editor) to run the flow manually and inspect each step's inputs and outputs. If an action fails, expand it to see the raw HTTP response — the `message` field usually explains exactly what went wrong.

![FX](./images/testpa.PNG)

### Common Errors

| Error | Likely cause |
|---|---|
| `403 Forbidden — required scopes: files` | PAT missing the `files` scope |
| `403 Forbidden — required scopes: jobs` | PAT missing the `jobs` scope |
| File arrives as 0 bytes | Body expression not evaluated via `fx` — sending JSON envelope instead of binary |
| `InvalidJson` on POST | Body is not valid JSON, or Content-Type is wrong |
