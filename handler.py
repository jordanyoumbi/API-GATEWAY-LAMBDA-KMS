import json
import boto3
import os

session = boto3.Session(
       region_name='', 
       aws_access_key_id='', 
       aws_secret_access_key=''
      )

ssm_client = session.client('ssm')
def getSecret(event, context):
    my_password = ssm_client.get_parameter(Name='jordan_kms', WithDecryption=True)
    return str(my_password)

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
