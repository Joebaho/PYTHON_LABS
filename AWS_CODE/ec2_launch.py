'''
AWS CODE: ec2_launch.py

Write a program that will launch one EC2 instance on the console
'''
# import boto3

# ec2 = boto3.resource('ec2')

# # Launch an EC2 instance
# instance = ec2.create_instances(
#     ImageId='ami-0c55b159cbfafe1f0',  # Specify your AMI ID
#     MinCount=1,
#     MaxCount=1,
#     InstanceType='t2.micro',
#     KeyName='your-key-pair'  # Specify your key-pair name
# )
# print(f'EC2 instance {instance[0].id} launched')

##########################################################################
# The second code include the majorities of properties for an Ec2 instances
import boto3

# Specify your AWS region
region = 'us-west-2'

# Initialize an EC2 resource
ec2 = boto3.resource('ec2', region_name=region)

# EC2 instance properties
ami_id = 'ami-033067239f2d2bfbc'  # Replace with a valid AMI ID for your region
instance_type = 't2.micro'         # Replace with your desired instance type
key_name = 'ansible-key'         # Replace with your key-pair name
security_group_ids = ['sg-03ca26bd2a3da94e7']  # Replace with your security group IDs
subnet_id = 'subnet-0afe31980b7b724ac'        # Replace with your subnet ID (optional)

# Launch an EC2 instance
instance = ec2.create_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    SubnetId=subnet_id,   # Optional: omit if you don't need to specify a subnet
    MinCount=1,           # Launch minimum 1 instance
    MaxCount=1,           # Launch maximum 1 instance
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'My-EC2-Instance'
                }
            ]
        }
    ]
    
)

# Print instance ID of the newly created instance
print(f'EC2 instance {instance[0].id} launched in {region} region.')
