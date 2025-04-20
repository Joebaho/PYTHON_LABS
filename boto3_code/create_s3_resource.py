import boto3

s3_resource = boto3.resource('s3') 
bucket_name = 'python-resource-bucket-02'
response = s3_resource.Bucket(bucket_name).create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    },
)
# Upload file
response = s3_resource.Bucket(bucket_name).upload_file('life_code.py', 'life_code.py' ) 
 
print(f"File uploaded successfully to {bucket_name}")
