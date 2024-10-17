'''
AWS CODE: object_S3_list.py

Write a program that will use AWS SNS (Simple Notification Service) to send an email notification using Python?.
'''
import boto3

sns = boto3.client('sns')

# Replace 'your-topic-arn' with your actual SNS topic ARN
response = sns.publish(
    TopicArn='your-topic-arn',
    Message='Hello, this is a test message from SNS',
    Subject='Test SNS Notification'
)

print("SNS notification sent!")

##########################################################################

import boto3

# Create an SNS client
sns = boto3.client('sns')

# Replace with your SNS topic ARN
topic_arn = 'arn:aws:sns:your-region:your-account-id:your-topic-name'

# Publish a message to the SNS topic
response = sns.publish(
    TopicArn=topic_arn,
    Message='Hello, this is a test message from SNS!',
    Subject='Test SNS Notification'
)

# Output the response (optional)
print(response)

