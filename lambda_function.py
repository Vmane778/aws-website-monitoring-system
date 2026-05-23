import json

def lambda_handler(event, context):
    """
    AWS Lambda function entry point.
    Args:
        event (dict): Event data passed to the function.
        context (LambdaContext): Runtime information.
    Returns:
        dict: Response object.
    """
    # Example response
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
