'''
AWS CODE: stop_start_ec2.py

Write a program that will terminate an EC2 instance using boto3.
'''
import boto3
from botocore.exceptions import ClientError

def terminate_ec2_instance(instance_id, region):

    ec2 = boto3.client('ec2', region_name=region)
    
    try:
        # Describe the instance to check if it exists and get its current state
        response = ec2.describe_instances(InstanceIds=[instance_id])
        if not response['Reservations']:
            print(f"Instance {instance_id} not found.")
            return False
        
        instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
        
        if instance_state == 'terminated':
            print(f"Instance {instance_id} is already terminated.")
            return True
        
        # Confirm termination
        confirm = input(f"Are you sure you want to terminate instance {instance_id}? (y/n): ")
        if confirm.lower() != 'y':
            print("Termination cancelled.")
            return False
        
        # Terminate the instance
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminating instance {instance_id}...")
        
        # Wait for the instance to be terminated
        waiter = ec2.get_waiter('instance_terminated')
        waiter.wait(InstanceIds=[instance_id])
        
        print(f"Instance {instance_id} has been terminated.")
        return True
    
    except ClientError as e:
        print(f"An error occurred: {e}")
        return False

def main():
    # Specify your instance ID and region
    instance_id = 'i-08a2e1e2fae19856f'  # Replace with your instance ID
    region = 'us-west-2'  # Replace with your region
    
    terminate_ec2_instance(instance_id, region)

if __name__ == '__main__':
    main()