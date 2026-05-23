import json
import time
import urllib3
import boto3
from datetime import datetime

# HTTP connection manager
http = urllib3.PoolManager()

# AWS services
sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

# Configuration
TABLE_NAME = 'WebsiteChecks'

TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

URL = "https://google.com"

EXPECTED_TEXT = "Google"

# DynamoDB table
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):

    start = time.time()

    status = "UP"
    error_message = ""

    try:

        # Send GET request
        response = http.request('GET', URL, timeout=5.0)

        # Calculate response time
        response_time = round((time.time() - start) * 1000)

        # Check status code
        if response.status != 200:
            status = "DOWN"
            error_message = f"Status code: {response.status}"

        # Read page content
        content = response.data.decode('utf-8')

        # Check expected content
        if EXPECTED_TEXT not in content:
            status = "BROKEN"
            error_message = "Expected content missing"

    except Exception as e:

        status = "DOWN"
        response_time = 0
        error_message = str(e)

    # Current timestamp
    timestamp = datetime.utcnow().isoformat()

    # Save result to DynamoDB
    table.put_item(
        Item={
            'website': URL,
            'timestamp': timestamp,
            'status': status,
            'response_time_ms': response_time,
            'error_message': error_message
        }
    )

    # Always send SNS alert
    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject='Website Status Alert',
        Message=f"""
Website check completed.

URL: {URL}
Status: {status}
Response Time: {response_time} ms
Error: {error_message}
"""
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'website': URL,
            'status': status,
            'response_time_ms': response_time
        })
    }
