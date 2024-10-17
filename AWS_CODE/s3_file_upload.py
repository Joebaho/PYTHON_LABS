'''
AWS CODE: s3_file_upload.py

Write a program that will upload a file in a S3 bucket using boto3.
'''

import boto3

s3 = boto3.client('s3')

# Upload file to S3
s3.upload_file('local_file.txt', 'your-bucket-name', 'remote_file.txt')
print("File uploaded successfully!")
