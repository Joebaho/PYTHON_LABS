'''
AWS CODE: ec2_launch.py

Write a program that will launch one EC2 instance on the console using function.

'''

import boto3
import time
import logging

# setup logger
# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(filename='my_ec2.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Initialize EC2 resource and client
region = 'us-west-2'  # You can change this to any desired region
ec2_resource = boto3.resource('ec2', region_name=region)


# EC2 instance properties
ami_id = 'ami-04907d7291cd8e06a'  # Replace with a valid AMI ID in your region
instance_type = 't2.micro'  # You can change the instance type if needed
key_name = 'ansible-key'  # Replace with your key pair name
security_group_ids = ['sg-03ca26bd2a3da94e7']  # Replace with your security group ID
subnet_id = 'subnet-0afe31980b7b724ac'  # Replace with your subnet ID if necessary

# Launch EC2 instance
def launch_ec2_instance():
    """
    Create or launch an EC2 instance on AWS.
     
    Parameters:
    instance_type (str): The type of EC2 instance to launch (e.g., "t2.micro").
    key_name (str): The name of the key pair to associate with the instance.
    security_group (str): The security group ID or name to associate with the instance.
    ami_id (str): The Amazon Machine Image (AMI) ID to use for the instance.
    region (str): The AWS region to launch the instance in (e.g., "us-west-2").

    Returns:
    dict: A dictionary containing details about the created instance, including instance ID and state.
    """
     
    instance = ec2_resource.create_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        #SecurityGroupIds=security_group_ids,
        #SubnetId=subnet_id,  # Optional: omit if you want default subnet
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'My-python-EC2'  # Replace with your desired instance name
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
    try:
        if instance:
             # Wait until instance is running
            instance_id = instance[0].id
            logger.info(f"EC2 instance {instance_id} launched. Waiting for it to be in running state...")

            instance[0].wait_until_running()
    
            # Reload the instance attributes
            instance[0].reload()

    # Get the public IP address of the instance
            public_ip_address = instance[0].public_ip_address
            logger.info(f"EC2 instance {instance_id} is running with Public IP Address: {public_ip_address}")
            # print(f"EC2 instance {instance[0].id} is being launched...")
            logger.info(f"EC2 instance {instance[0].id} is being launched...")
        
    except Exception as e:
        # print(f"An error occurred while creating or writing to the file '{filename}': {e}")
        logger.error(f"An error occurred while creating instance '{instance_id}': {e}")
    
    print(f"EC2 instance {instance_id} is running with Public IP Address: {public_ip_address}")

# Call the function to launch the EC2 instance
launch_ec2_instance()
