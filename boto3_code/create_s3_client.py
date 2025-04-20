import boto3

# Define your S3 client
s3_client = boto3.client('s3', region_name='us-west-2')  # Set the region you want

# Define the bucket name
bucket_name = "python-client-bucket-01"

# Create the bucket with the appropriate location constraint
response = s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'  # Match the region you specified in the client
    }
)
print("Bucket created successfully:", response)
#upload file in the bucket 
s3_client.upload_file('life_code.py', 'python-client-bucket-01', 'life_code.py')



