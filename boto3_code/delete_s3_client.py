import boto3

s3_client = boto3.client('s3') 
bucket_name = 'python-client-bucket-01'
# List and delete all objects in the bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
        print(f"Deleted object: {obj['Key']}")

# Delete the empty bucket
response = s3_client.delete_bucket(Bucket=bucket_name)
print(f"Bucket {bucket_name} deleted successfully")