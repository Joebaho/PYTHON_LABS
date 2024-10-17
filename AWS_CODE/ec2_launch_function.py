'''
AWS CODE: ec2_launch.py

Write a program that will launch one EC2 instance on the console using function.

'''

import boto3
import time

# Initialize EC2 resource and client
region = 'us-west-2'  # You can change this to any desired region
ec2_resource = boto3.resource('ec2', region_name=region)
ec2_client = boto3.client('ec2', region_name=region)

# EC2 instance properties
ami_id = 'ami-08d8ac128e0a1b91c'  # Replace with a valid AMI ID in your region
instance_type = 't2.micro'  # You can change the instance type if needed
key_name = 'ansible-key'  # Replace with your key pair name
security_group_ids = ['sg-03ca26bd2a3da94e7']  # Replace with your security group ID
subnet_id = 'subnet-0afe31980b7b724ac'  # Replace with your subnet ID if necessary

# Launch EC2 instance
def launch_ec2_instance():
    instance = ec2_resource.create_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        #SecurityGroupIds=security_group_ids,
        #SubnetId=subnet_id,  # Optional: omit if you want default subnet
        MinCount=1,
        MaxCount=3,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'My-Launched-EC2'  # Replace with your desired instance name
                    }
                ]
            }
        ],
        # Enabling public IP address
        NetworkInterfaces=[{
            'DeviceIndex': 0,
            'SubnetId': subnet_id,
            'AssociatePublicIpAddress': True,
            'Groups': security_group_ids
        }]
    )

    # Wait until instance is running
    instance_id = instance[0].id
    print(f"EC2 instance {instance_id} launched. Waiting for it to be in running state...")

    instance[0].wait_until_running()
    
    # Reload the instance attributes
    instance[0].reload()

    # Get the public IP address of the instance
    public_ip_address = instance[0].public_ip_address
    print(f"EC2 instance {instance_id} is running with Public IP Address: {public_ip_address}")

# Call the function to launch the EC2 instance
launch_ec2_instance()
