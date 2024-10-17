'''
AWS CODE: cloudformation_detect_drift.py

Write a Python function to detect drift: 

'''
def detect_stack_drift(stack_name):
    cf_client = boto3.client('cloudformation')
    
    try:
        # Initiate drift detection
        response = cf_client.detect_stack_drift(StackName=stack_name)
        drift_detection_id = response['StackDriftDetectionId']
        
        # Wait for drift detection to complete
        while True:
            response = cf_client.describe_stack_drift_detection_status(
                StackDriftDetectionId=drift_detection_id
            )
            if response['DetectionStatus'] == 'DETECTION_COMPLETE':
                break
            time.sleep(5)
        
        # Print drift status
        print(f"Stack Drift Status: {response['StackDriftStatus']}")
        
        if response['StackDriftStatus'] == 'DRIFTED':
            # Get drifted resources
            resources = cf_client.describe_stack_resource_drifts(StackName=stack_name)
            for resource in resources['StackResourceDrifts']:
                if resource['StackResourceDriftStatus'] == 'MODIFIED':
                    print(f"Resource {resource['LogicalResourceId']} has drifted")
    
    except Exception as e:
        print(f"Error detecting drift: {str(e)}")

# Detect drift
detect_stack_drift('MyS3BucketStack')