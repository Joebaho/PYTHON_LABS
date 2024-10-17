'''
AWS CODE: s3_file_triggered.py

Write a program that will Lambda with S3 Trigger: 
Set up an AWS Lambda function that is triggered when a new file is uploaded to an S3 bucket and processes the file (e.g., converts it from one format to another or extracts metadata).
'''
import json
import boto3
import os
from datetime import datetime

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        # Get the object
        response = s3_client.get_object(Bucket=bucket, Key=key)
        
        # Extract metadata
        metadata = {
            'filename': key,
            'size': response['ContentLength'],
            'last_modified': response['LastModified'].isoformat(),
            'content_type': response.get('ContentType', 'Unknown'),
        }
        
        # If it's a text file, you could read its contents
        if metadata['content_type'].startswith('text/'):
            file_content = response['Body'].read().decode('utf-8')
            metadata['first_line'] = file_content.split('\n')[0] if file_content else ''
        
        # Save metadata to another bucket
        destination_bucket = os.environ['DESTINATION_BUCKET']
        metadata_key = f"metadata/{key.split('/')[-1]}.json"
        
        s3_client.put_object(
            Bucket=destination_bucket,
            Key=metadata_key,
            Body=json.dumps(metadata, indent=2),
            ContentType='application/json'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Metadata extracted and saved for {key}")
        }
    
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing {key}: {str(e)}")
        }