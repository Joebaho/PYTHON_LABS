'''
AWS CODE: cloudformation_stack_delete.py

Write a program that will delete an existing stack: 
The stack is a S3 bucket.
'''
def delete_stack(stack_name):
    cf_client = boto3.client('cloudformation')
    
    try:
        cf_client.delete_stack(StackName=stack_name)
        print(f"Stack deletion initiated for {stack_name}")
        
        # Wait for the stack to be deleted
        waiter = cf_client.get_waiter('stack_delete_complete')
        print("Waiting for stack deletion to complete...")
        waiter.wait(StackName=stack_name)
        
        print("Stack deleted successfully.")
    except Exception as e:
        print(f"Error deleting stack: {str(e)}")

# Delete the stack
delete_stack('MyS3BucketStack')