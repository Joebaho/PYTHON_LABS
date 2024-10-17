'''
AWS CODE: ec2_launch.py

Write a program that will launch five EC2 instances on the console using function and loop.

'''
import boto3

# Initialize EC2 resource and client
region = 'us-west-2'  # Change this to your desired region
ec2_resource = boto3.resource('ec2', region_name=region)
ec2_client = boto3.client('ec2', region_name=region)

# EC2 instance properties
ami_id = 'ami-08d8ac128e0a1b91c'  # Replace with a valid AMI ID in your region
instance_type = 't2.micro'  # You can change the instance type if needed
key_name = 'Oregon_key_pair'  # Replace with your key pair name
security_group_ids = ['sg-03ca26bd2a3da94e7']  # Replace with your security group ID

# List of Subnet IDs for 3 different Availability Zones (AZs) - Ensure subnets are in 3 different AZs
subnet_ids = ['subnet-0fe2192064551316c', 'subnet-0afe31980b7b724ac', 'subnet-099fca76d17b2fd4f']  # Replace with your subnets

# Number of instances to launch
total_instances = 5

# Launch EC2 instances across different AZs
def launch_ec2_instances():
    launched_instances = []

    for i in range(total_instances):
        # Distribute instances across different subnets/AZs
        subnet_id = subnet_ids[i % len(subnet_ids)]  # Cycle through the subnets
        
        print(f"Launching instance {i + 1} in subnet: {subnet_id}...")

        instance = ec2_resource.create_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': f'Instance-{i + 1}'  # Assign different names to each instance
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

        launched_instances.append(instance[0])

    return launched_instances

# Wait for the instances to be running and display their public IP addresses
def display_instance_info(instances):
    for instance in instances:
        instance_id = instance.id
        print(f"Waiting for instance {instance_id} to be in running state...")

        instance.wait_until_running()
        instance.reload()

        # Get the public IP address of the instance
        public_ip_address = instance.public_ip_address
        print(f"Instance {instance_id} is running with Public IP Address: {public_ip_address}")

# Launch the EC2 instances
launched_instances = launch_ec2_instances()

# Display their public IPs once they are running
display_instance_info(launched_instances)
