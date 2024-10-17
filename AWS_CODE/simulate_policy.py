'''
AWS CODE: simple_lambda_function.py

Write a program that will simulate a policy:
'''
import boto3

def simulate_policy(policy_document, action, resource):
    iam = boto3.client('iam')
    try:
        response = iam.simulate_custom_policy(
            PolicyInputList=[policy_document],
            ActionNames=[action],
            ResourceArns=[resource]
        )
        for result in response['EvaluationResults']:
            print(f"Action: {result['EvalActionName']}")
            print(f"Decision: {result['EvalDecision']}")
    except Exception as e:
        print(f"Error simulating policy: {str(e)}")

# Usage
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::example-bucket/*"
        }
    ]
}

simulate_policy(json.dumps(policy), "s3:GetObject", "arn:aws:s3:::example-bucket/file.txt")