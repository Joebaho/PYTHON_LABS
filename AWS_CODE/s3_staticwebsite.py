'''
AWS CODE: s3_file_upload.py

Write a program that will create a S3 bucket that will be use for a static website using boto3.
'''
import boto3
import json
from botocore.exceptions import ClientError

# Region to launch
region = 'us-west-2' 

def create_bucket(bucket_name, region=None):
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        print(e)
        return False
    return True

def configure_website(bucket_name):
    """Configure S3 bucket for static website hosting"""
    s3 = boto3.client('s3')
    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'},
    }
    s3.put_bucket_website(Bucket=bucket_name,
                          WebsiteConfiguration=website_configuration)

def set_bucket_policy(bucket_name):
    """Set bucket policy to allow public read access"""
    s3 = boto3.client('s3')
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'PublicReadGetObject',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }]
    }
    policy_string = json.dumps(bucket_policy)
    s3.put_bucket_policy(Bucket=bucket_name, Policy=policy_string)

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(e)
        return False
    return True

def main():
    bucket_name = 'my-static-website-bucket-12345'  # Must be globally unique
    region = 'us-west-2'  # Choose your preferred region

    # Create the bucket
    if create_bucket(bucket_name, region):
        print(f"Bucket {bucket_name} created successfully")
    else:
        print(f"Failed to create bucket {bucket_name}")
        return

    # Configure for static website hosting
    configure_website(bucket_name)
    print("Configured bucket for static website hosting")

    # Set bucket policy
    set_bucket_policy(bucket_name)
    print("Set bucket policy for public read access")

    # Create a simple index.html file
    with open('index.html', 'w') as f:
        f.write('<html><body><h1>Hello, World!</h1></body></html>')

    # Upload the file
    if upload_file('index.html', bucket_name):
        print("Uploaded index.html successfully")
    else:
        print("Failed to upload index.html")

    print(f"Website URL: http://{bucket_name}.s3-website-{region}.amazonaws.com")

if __name__ == '__main__':
    main()