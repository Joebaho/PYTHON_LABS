'''
Write two functions: the first one to create a text file called "python-on-aws.txt" containing the text below: "programming is fun, but you got to practice". 
The second function to upload the file created previously to any existing S3 bucket on AWS.
''' 
import boto3


def create_file(file_name, content):
    """
    Creates a file and add a content inside it.
    
    Parameters:
    file_name (str): Name of the file to be created 
    content (str): Content to be written in the file
    
    Returns:
    str: Name of the created file
    """
    # Create the file
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' has been created successfully.")
    return file_name
# Vatiables
file_name = 'python-on-aws.txt'
content = "programming is fun, but you got to practice"
# Calling the function
create_file(file_name, content)
    
def upload_file(bucket_name, file_name):
     """
    Upload the file created previously to any existing S3 bucket on AWS.
    
    
    Parameters:
    file_name (str): Name of the file to be created 
    bucket_name (str): Name of the bucket to upload the file to
    
    Returns:
    str: Name of the created file
    """
    # Upload the file to S3
     s3 = boto3.client('s3')
     try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"File '{file_name}' has been uploaded to '{bucket_name}' successfully.")
       
     except Exception as e:
        print(f"Error uploading file: {e}")
        
# Variables
bucket_name = 'baho-backup-bucket'
file_name = 'python-on-aws.txt'
#calling the function
upload_file(bucket_name, file_name)
