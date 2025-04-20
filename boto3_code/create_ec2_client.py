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
ec2_client = boto3.client('ec2', region_name=region)

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
     
    instance = ec2_client.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        #SecurityGroupIds=security_group_ids,
        #SubnetId=subnet_id,  # Optional: omit if you want default subnet
        MinCount=1,
        MaxCount=1,
        Monitoring={
                'Enabled': False
            },
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'EC2-created-by-python'  # Replace with your desired instance name
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
            instance_id = instance['Instances'][0]['InstanceId']
            logger.info(f"EC2 instance {instance_id} launched. Waiting for it to be in running state...")

            instance[0].wait_until_running()
    
            # Reload the instance attributes
            instance[0].reload()

    # Get the public IP address of the instance
            instance_description = ec2_client.describe_instances(InstanceIds=[instance_id])
            public_ip = instance_description['Reservations'][0]['Instances'][0]['PublicIpAddress']
            logger.info(f"EC2 instance {instance_id} is running with Public IP Address:{public_ip} ")
            # print(f"EC2 instance {instance[0].id} is being launched...")
            logger.info(f"EC2 instance {instance[0].id} is being launched...")
        
    except Exception as e:
        # print(f"An error occurred while creating or writing to the file '{filename}': {e}")
        logger.error(f"An error occurred while creating instance {instance_id}: {e}")
    
    print(f"EC2 instance {instance_id} is running with Public IP Address: {public_ip}")

# Call the function to launch the EC2 instance
if __name__ == "__main__":
  launch_ec2_instance()

#####################################################################################################################  

import boto3
import logging

# setup logger
# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(filename='testingapp.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

def create_ec2(instance_type='t3.micro', image_id='ami-061dd8b45bc7deb3d',subnet_id='subnet-0fe2192064551316c', key_name='ansible-key'): 
    '''
    create an EC2 instance with the name ec2-created-by-python

    Parameters:
    - Instance Type : str
    - image_id : str
    - subnet_id: str

    Returns:
    - Dict: Reponse with the EC2 created info
    '''


    # Initialize the ec2 client
    ec2 = boto3.client('ec2')
    
    try:
        response = ec2.run_instances(
            InstanceType = instance_type, 
            ImageId = image_id,
            MaxCount = 1,
            MinCount = 1,
            KeyName = key_name,
            Monitoring={
                'Enabled': False
            },
            NetworkInterfaces=[
               {
                   'AssociatePublicIpAddress': True,
                   'DeviceIndex': 0,
                   'Groups': ['sg-03ca26bd2a3da94e7'],
                   'SubnetId': subnet_id
               }
            ],   
            TagSpecifications=[
                {
                    'ResourceType':'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'ec2-created-by-python'
                        }
                    ]
                }
            ]
        )
        logger.info(f"EC2 instance with InstanceType {instance_type} and Amazon ami ID {image_id} is created  ")
        return response

    except Exception as e:
        logger.error(f"Error creating EC2 instance: {str(e)}")
    
# main
if __name__ == "__main__":
    create_ec2()
    logger.info(f"The ec2 was created successfully")