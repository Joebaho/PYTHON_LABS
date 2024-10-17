'''
AWS CODE: cloudformation_deploy.py

Write a program that will deploys a CloudFormation stack using the template given: 
Template is creating a S3 bucket.
'''
import boto3
import time

def create_stack(stack_name, template_body):
    cf_client = boto3.client('cloudformation')
    
    try:
        response = cf_client.create_stack(
            StackName=stack_name,
            TemplateBody=template_body,
            Capabilities=['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM'],
        )
        
        print(f"Stack creation initiated. Stack ID: {response['StackId']}")
        
        # Wait for the stack to complete
        waiter = cf_client.get_waiter('stack_create_complete')
        print("Waiting for stack to complete...")
        waiter.wait(StackName=stack_name)
        
        print("Stack creation completed successfully.")
    except Exception as e:
        print(f"Error creating stack: {str(e)}")

# Read the template from a file
with open('s3_bucket_template.yaml', 'r') as file:
    template_body = file.read()

# Create the stack
create_stack('MyS3BucketStack', template_body)