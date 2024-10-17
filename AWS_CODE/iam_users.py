'''
AWS CODE: cost_reporting.py

Write a program that will create, list, and delete IAM users
'''
import boto3

def create_user(username):
    iam = boto3.client('iam')
    try:
        response = iam.create_user(UserName=username)
        print(f"User {username} created successfully")
        return response['User']
    except Exception as e:
        print(f"Error creating user: {str(e)}")

def list_users():
    iam = boto3.client('iam')
    try:
        response = iam.list_users()
        for user in response['Users']:
            print(f"Username: {user['UserName']}, Created: {user['CreateDate']}")
    except Exception as e:
        print(f"Error listing users: {str(e)}")

def delete_user(username):
    iam = boto3.client('iam')
    try:
        iam.delete_user(UserName=username)
        print(f"User {username} deleted successfully")
    except Exception as e:
        print(f"Error deleting user: {str(e)}")

# Usage
create_user('new_user')
list_users()
delete_user('new_user')