'''
AWS CODE: cost_reporting.py

Write a program that will create an IAM role for EC2 instances:
'''
import boto3
import json

def create_ec2_role(role_name):
    iam = boto3.client('iam')
    
    trust_relationship = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "ec2.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
        ]
    }
    
    try:
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_relationship)
        )
        print(f"Role {role_name} created successfully")
        return response['Role']
    except Exception as e:
        print(f"Error creating role: {str(e)}")

# Usage
create_ec2_role('MyEC2Role')