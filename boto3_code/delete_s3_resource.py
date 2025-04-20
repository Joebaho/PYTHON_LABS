import boto3

s3_resource = boto3.resource('s3') 
bucket_name = 'python-resource-bucket-02'
response =s3_resource.Bucket(bucket_name).delete()
print (response)

