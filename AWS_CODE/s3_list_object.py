'''
AWS CODE: object_S3_list.py

Write a program that will list object in a S3 bucket.
'''

import boto3

s3 = boto3.client('s3')

# Replace 'your-bucket-name' with your actual bucket
response = s3.list_objects_v2(Bucket='your-bucket-name')

for obj in response.get('Contents', []):
    print(obj['Key'])
