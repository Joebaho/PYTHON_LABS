'''
AWS CODE: cloudformation_deploy.py

Write a program that will update an existing stack: 
The stack is a S3 bucket.
'''
def update_stack(stack_name, template_body):
    cf_client = boto3.client('cloudformation')
    
    try:
        response = cf_client.update_stack(
            StackName=stack_name,
            TemplateBody=template_body,
            Capabilities=['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM'],
        )
        
        print(f"Stack update initiated. Stack ID: {response['StackId']}")
        
        # Wait for the stack to complete
        waiter = cf_client.get_waiter('stack_update_complete')
        print("Waiting for stack update to complete...")
        waiter.wait(StackName=stack_name)
        
        print("Stack update completed successfully.")
    except Exception as e:
        print(f"Error updating stack: {str(e)}")

# Update the stack
update_stack('MyS3BucketStack', update_template_body)