'''
AWS CODE: ec2_client_describe.py

Write a program that will list all EC2 instances in your region
and show the must important parameters of each instance using boto3.
 
'''

import boto3

def list_ec2_instances():
    """
    List all EC2 instances and their states using boto3.

    Parameters:

    Returns:
    
    """
    # Initialize EC2 client
    ec2_client = boto3.client('ec2')
    
    # Describe EC2 instances
    response = ec2_client.describe_instances()
    
    for reservation in response['Reservations']:
      for instance in reservation['Instances']:
        print("-------------------------------------------------")
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Name: {instance['Tags'][0]['Value']}")
        print(f"Instance State: {instance['State']['Name']}")
        print(f"Instance keypair: {instance['KeyName']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"Instance AZ : {instance['Placement']['AvailabilityZone']}")
        print(f"Instance Monitoring State: {instance['Monitoring']['State']}")
        print(f"Instance Subnet: {instance['SubnetId']}")
        print(f"Instance VPC: {instance['VpcId']}")
        print(f"Instance Public IP Address: {instance['PublicIpAddress']}")
        print(f"Instance Date and Time Launched: {instance["LaunchTime"]}")
        print("-------------------------------------------------")
        
if __name__ == "__main__":
    list_ec2_instances()

