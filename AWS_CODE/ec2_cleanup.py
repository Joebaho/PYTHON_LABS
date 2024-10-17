'''
AWS CODE: ec2_launch.py

Write a program that will Automated EC2 Resource Cleanup: 
Write a Python script using Boto3 to identify and stop/terminate EC2 instances 
that have been running for a specific time to avoid unnecessary charges.
'''

import boto3
from datetime import datetime, timedelta
import pytz

def cleanup_ec2_instances(max_runtime_hours, region, dry_run=True):
    ec2 = boto3.resource('ec2', region_name=region)
    client = boto3.client('ec2', region_name=region)

    # Get current time in UTC
    now = datetime.now(pytz.utc)

    print(f"Identifying EC2 instances running for more than {max_runtime_hours} hours...")

    for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
        launch_time = instance.launch_time
        runtime = now - launch_time.replace(tzinfo=pytz.utc)

        if runtime > timedelta(hours=max_runtime_hours):
            print(f"Instance {instance.id} has been running for {runtime}")
            
            try:
                if dry_run:
                    print(f"Dry run: Would stop instance {instance.id}")
                else:
                    client.stop_instances(InstanceIds=[instance.id])
                    print(f"Stopped instance {instance.id}")
                
                # Uncomment the following lines if you want to terminate instead of stop
                # if dry_run:
                #     print(f"Dry run: Would terminate instance {instance.id}")
                # else:
                #     client.terminate_instances(InstanceIds=[instance.id])
                #     print(f"Terminated instance {instance.id}")

            except Exception as e:
                print(f"Error processing instance {instance.id}: {str(e)}")

if __name__ == "__main__":
    # Configuration
    MAX_RUNTIME_HOURS = 24  # Adjust this to your desired maximum runtime
    REGION = 'us-west-2'    # Change this to your desired AWS region
    DRY_RUN = True          # Set to False to actually stop/terminate instances

    cleanup_ec2_instances(MAX_RUNTIME_HOURS, REGION, DRY_RUN)