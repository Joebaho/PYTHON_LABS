'''
AWS CODE: s3_file_upload.py

Write a program that will create a S3 bucket using boto3.
'''
import boto3
from botocore.exceptions import ClientError

# Region to launch
region = 'us-west-2' 

def create_s3_bucket(bucket_name, region):
    # Create boto3 client
    s3_client = boto3.client('s3', region_name=region) if region else boto3.client('s3')

    try:
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        print(f"An error occurred: {e}")
        return False
    return True

def main():
    # Specify your bucket name and region
    bucket_name = 'python-s3-bucket-created'  # Must be globally unique
    region = 'us-west-2'  # e.g., 'us-west-2', 'eu-west-1'. Use None for us-east-1

    if create_s3_bucket(bucket_name, region):
        print(f"Bucket '{bucket_name}' created successfully in region '{region or 'us-east-1'}'")
    else:
        print(f"Bucket creation failed")

if __name__ == '__main__':
    main()