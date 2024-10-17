'''
AWS CODE: sqs_retrieve.py

Write a program that will retrieve a Message from an SQS Queue.
'''
import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Replace with your SQS queue URL
queue_url = 'https://sqs.your-region.amazonaws.com/your-account-id/your-queue-name'

# Receive a message from the SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,  # Receive at most one message (can change based on your needs)
    WaitTimeSeconds=10      # Wait time in seconds for long polling
)

# Check if a message was received
messages = response.get('Messages', [])
if messages:
    # Extract message details
    message = messages[0]
    receipt_handle = message['ReceiptHandle']
    message_body = message['Body']

    print(f"Received message: {message_body}")

    # Delete the message after processing it
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print("Message deleted from the queue.")
else:
    print("No messages available.")
