'''
AWS CODE: stop_start_ec2.py

Write a program that will start and stop an EC2 instance using boto3.
'''
import boto3

ec2 = boto3.client('ec2')

# Replace 'instance_id' with your actual EC2 instance ID
instance_id = 'i-02ec02980aa372f9c'

# Start the instance
ec2.start_instances(InstanceIds=[instance_id])
print(f'Starting EC2 instance {instance_id}...')

# Stop the instance
ec2.stop_instances(InstanceIds=[instance_id])
print(f'Stopping EC2 instance {instance_id}...')
