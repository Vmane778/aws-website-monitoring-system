# Screenshot 1: AWS Lambda Function - website-monitor

This screenshot shows the AWS Lambda function code for the website monitoring system.

**Key Details:**
- Function Name: `website-monitor`
- Handler: `lambda_function.lambda_handler(event, context)`
- Language: Python
- Code Source: Visible in AWS Lambda console

**Visible Code Section (lines 27-88):**
The lambda handler function includes:
- Line 27: Function definition
- Line 76-87: SNS publish message with website check results
  - Message includes: URL, Status, Response Time, Error information
  
**Response Example:**
```json
{
  "statusCode": 200,
  "body": {
    "website": "https://google.com",
    "status": "UP",
    "response_time_ms": 721
  }
}
```

**Execution Results:**
- Last 4 KB of execution log visible
- Function Logs show START and END RequestId
- RequestId: c7d59dff-fac9-47c6-845d-4dad49f9441c

**Available Actions:**
- Deploy (⌘$U)
- Test (⌘$⌘I)
- Deploy dropdown menu
- Test Events section with saved test events
