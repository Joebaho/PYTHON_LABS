'''
AWS CODE: simple_lambda_function.py

Write a program that will launch a simple lambda function.
'''

import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
