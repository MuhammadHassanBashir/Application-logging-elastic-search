# Application logging on elastic cloud using fluentd as log collector

## Objective:

This document outlines the process of logging application events and sending alerts to Microsoft Teams. The logging process involves sending logs directly from the application to a specific endpoint, which is a virtual machine (VM) hosted on Google Cloud Platform (GCP).Within this VM, Fluentd is configured to collect application logs and forward them to Elastic Cloud. Subsequently, we set up alerts in Elastic Cloud to send error logs to a Microsoft Teams channel.

### logger.py

Check python code availble on file logger.py. With this we are sending application logs to GCP Vm..

### Fluentd Configuration

Check fluent.conf file for fluentd configuration. We are running container on GCP vm having fluentd images with this configuration.

### Sending Alerts to Microsoft Teams:

-  Create a chennel in MS Team to receiving alerts.  
-  Configure and use webhook in Microsoft Teams to receive alerts on created channel.
-  Set up alerts in Elastic Cloud to trigger on error logs.
-  Configure the alert to use the previously created webhook URL for sending alerts to the Teams channel.

### Manual Verification:

Execute the provided Python code to manually verify that logs are successfully sent to the specified endpoint.

### Conclusion:

By following the outlined process, application logging is effectively managed, and alerts are sent to Microsoft Teams for timely response to error events. This ensures better monitoring and troubleshooting
