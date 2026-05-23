# AWS Website Monitoring System

A serverless website monitoring and alerting platform built on AWS using Lambda, DynamoDB, SNS, and CloudWatch.

## Features

- Website uptime monitoring
- Responsetime tracking
- Content validation checks
- Real-time email alerts
- Historical monitoring logs
- Serverless architecture

## AWS Services Used

- AWS Lambda
- Amazon SNS
- Amazon DynamoDB
- Amazon CloudWatch
  

## Architecture

Lambda checks website health and:
1. Stores monitoring results in DynamoDB
2. Sends alerts using SNS
3. Logs execution in CloudWatch

## Example Monitoring Data

```json
{
  "website": "https://google.com",
  "status": "UP",
  "response_time_ms": 245
}
```
