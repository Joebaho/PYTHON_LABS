'''
AWS CODE: s3_cleanup.py

Write a program that will S3 Bucket Cleaner: 
Create a script that deletes old files (e.g., older than 30 days) from an S3 bucket to save storage costs.
'''
import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError

def delete_old_files(bucket_name, days_threshold, prefix='', dry_run=True):
    """
    Delete files older than the specified threshold from an S3 bucket.
    :param bucket_name: Name of the S3 bucket
    :param days_threshold: Files older than this many days will be deleted
    :param prefix: Optional prefix to filter objects (e.g., folder path)
    :param dry_run: If True, only print actions without deleting
    """
    s3 = boto3.client('s3')
    
    # Calculate the threshold date
    threshold_date = datetime.now() - timedelta(days=days_threshold)
    
    # Use paginator to handle buckets with many objects
    paginator = s3.get_paginator('list_objects_v2')
    
    total_deleted = 0
    total_size_deleted = 0
    
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        if 'Contents' not in page:
            continue
        
        for obj in page['Contents']:
            if obj['LastModified'] < threshold_date:
                if dry_run:
                    print(f"Would delete: {obj['Key']} (Last modified: {obj['LastModified']})")
                else:
                    try:
                        s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                        print(f"Deleted: {obj['Key']} (Last modified: {obj['LastModified']})")
                        total_deleted += 1
                        total_size_deleted += obj['Size']
                    except ClientError as e:
                        print(f"Error deleting {obj['Key']}: {e}")
    
    print(f"\nTotal objects {'that would be' if dry_run else ''} deleted: {total_deleted}")
    print(f"Total size {'that would be' if dry_run else ''} freed: {total_size_deleted / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    # Configuration
    BUCKET_NAME = 'your-bucket-name'
    DAYS_THRESHOLD = 30
    PREFIX = ''  # Optional: set this to a folder path if you want to clean a specific folder
    DRY_RUN = True  # Set to False to actually delete files
    
    delete_old_files(BUCKET_NAME, DAYS_THRESHOLD, PREFIX, DRY_RUN)
