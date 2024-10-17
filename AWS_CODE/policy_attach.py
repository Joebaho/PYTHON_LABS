'''
AWS CODE: object_S3_list.py

Write a program that will attach a policy to a role:
'''
import boto3

def attach_policy_to_role(role_name, policy_arn):
    iam = boto3.client('iam')
    try:
        iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        print(f"Policy {policy_arn} attached to role {role_name}")
    except Exception as e:
        print(f"Error attaching policy: {str(e)}")

# Usage
attach_policy_to_role('MyEC2Role', 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')