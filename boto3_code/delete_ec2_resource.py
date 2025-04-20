'''
AWS CODE: terminate_ec2_resource.py

Write a program that will terminate an EC2 instance using boto3.
'''
import boto3
from botocore.exceptions import ClientError 
import logging

# Setup logger
logging.basicConfig(
    filename='my_ec2.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def terminate_ec2_instance(instance_id, region):
    """
    Terminate an EC2 instance on AWS.

    Parameters:
    instance_id (str): The ID of the instance to terminate.
    region (str): The AWS region where the instance is located.

    Returns:
    bool: True if the instance is terminated successfully, False otherwise.
    """
    ec2 = boto3.resource('ec2', region_name=region)

    try:
        # Fetch the instance
        instance = ec2.Instance(instance_id)

        # Confirm termination
        confirm = input(f"Are you sure you want to terminate instance {instance_id}? (y/n): ")
        if confirm.lower() != 'y':
            print("Termination cancelled.")
            return False

        # Terminate the instance
        response = instance.terminate()
        logger.info(f"Termination initiated for instance {instance_id}. Response: {response}")
        
        # Wait for termination
        instance.wait_until_terminated()
        logger.info(f"Instance {instance_id} has been terminated.")
        print(f"Instance {instance_id} has been terminated.")
        return True

    except ClientError as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
        return False

def main():
    """
    Provide information on the EC2 instance on AWS that will be terminate.
     
    Parameters:
    
    ami_id (str): The Amazon Machine Image (AMI) ID to use for the instance.
    region (str): The AWS region to launch the instance in (e.g., "us-west-2").

    Returns:
    str: A sentence describing the termination of the instance, including instance status.
    """
    instance_id = 'i-07805319084b2e767'  # Replace with your instance ID
    region = 'us-west-2'  # Replace with your region

    # Terminate the instance
    terminate_ec2_instance(instance_id, region)

if __name__ == '__main__':
    main()
