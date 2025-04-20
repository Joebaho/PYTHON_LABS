import boto3

def cleanup(bucket_name):
    s3 = boto3.resource('s3')
    try:
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()  # Empty bucket first
        bucket.delete()                # Then delete bucket
        print(f"✅ Successfully deleted {bucket_name}")
    except Exception as e:
        print(f"❌ Error deleting {bucket_name}: {e}")

if __name__ == '__main__':
    cleanup("your-bucket-name-here")  # Replace with your bucket name