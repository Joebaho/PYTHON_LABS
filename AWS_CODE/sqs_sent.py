'''
AWS CODE: sqs.py

Write a program that will Send a Message to an SQS Queue.
'''
import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Replace with your SQS queue URL
queue_url = 'https://sqs.your-region.amazonaws.com/your-account-id/your-queue-name'

# Send a message to the SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='This is a test message for SQS!'
)

# Output the response (optional)
print(response)
