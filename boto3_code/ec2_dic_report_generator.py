'''
AWS CODE: ec2_report_generator.py

Write a program that will list all EC2 instances and their states using boto3.
Then copy the report to an csv file, email it to a specified email address 
and send it in a S3 bucket created . Result will be a Dictionary.
'''
# Import all neccesssary libraries
import boto3
import botocore
import csv
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

# setup logger
logging.basicConfig(filename='ec2_report.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Declare global variables
FILE_NAME = 'ec2_report.csv'
BUCKET_NAME = 'python-ec2-report-generator-bucket1'
TOP_EMAIL ='joebachou@gmail.com'
TOP_PWD ='adzb ulso elxn zpyc'
CC_EMAIL = ['info@cloudspaceacademy.com', 'josephmbatchou2@gmail.com']
current_date = datetime.now().strftime("%Y-%m-%d")

#First function 
def list_ec2_instances():
    """
    Gather all ec2 instance
    :param
    :return
    """
    # create an empty dictionary
    list_ec2_instances = {}

    # Initialize client
    ec2_client = boto3.client('ec2')

    # response
    response = ec2_client.describe_instances()

    # retrieve the list of instances
    reservations = response['Reservations'] # list with 2 dictionaries

    # looping through the reservations
    for reservation in reservations:
        # we need to loop to retrieve instances
        for instance in reservation["Instances"]:
            instance_id = instance['InstanceId']
            name=instance['Tags'][0]['Value']
            state = instance['State']['Name']
            instance_type = instance['InstanceType']
            key_name=instance['KeyName']
            availability_zone=instance['Placement']['AvailabilityZone']
            monitoring=instance['Monitoring']['State']
            vpc_id=instance['VpcId']
            subnet_id=instance['SubnetId']
            public_ip=instance['PublicIpAddress']
            launch_time=instance['LaunchTime']
            
            # Add all element to the dictionary
            list_ec2_instances.update({'Instance_Id': instance_id, 'Name': name, 'State': state, 'Instance_Type':instance_type, 'Key_Name':key_name, 'Availability_Zone': availability_zone, 'Monitoring': monitoring, 'Vpc_Id':vpc_id, 'Subnet_Id':subnet_id, 'Public_Ip':public_ip, 'Launch_Time':launch_time })
            
    return list_ec2_instances

# Second Function: Generate cvs report file
def generate_csv_report(instances):
    """
        This function will generate a csv report per Micheal
        :param list of instances
        :return return true if valid
    """
    try:
        with open(FILE_NAME, 'w', newline='') as csvfile:
            fieldnames = ['Instance_Id', 'Name', 'State', 'Instance_Type', 'Key_Name', 'Availability_Zone', 'Monitoring', 'Vpc_Id', 'Subnet_Id', 'Public_Ip', 'Launch_Time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerow(instances) 
                
    except OSError as error:
        logger.error(f"The file wasn't found! {error}")
        return False
    return True # optional

# Third Function: Upload file to s3 bucket
def upload_report_to_s3():
    """
        This function will upload csv report to s3 bucket
        :param 
        :return 
    """
    
    s3_client = boto3.client('s3')

    try:
        s3_client.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
    except botocore.exceptions.ClientError as error:
        logger.error(f"Something happened while uploading the file {error}")

#Fourth Function : send email
def send_email():
    """
        This function will send email to specified email address
        :param
        :return
    """

    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = TOP_EMAIL
        msg['To'] = ', '.join(CC_EMAIL)
        msg['Subject'] = f"EC2 Instances Report - {current_date}"
        body = f"""
        Hello,

        Hope this email finds you well? Please find attached the EC2 instances report generated on {current_date}.

        Best regards,

          Joseph Mbatchou
        Cloud & DevOps Engineer
         Hollister, CA 95023
          +1(408)-449-9131
         https://www.joebahocloud.com

        """

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach the CSV file
        with open(FILE_NAME, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={FILE_NAME}'
            )
            msg.attach(part)

        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(TOP_EMAIL, TOP_PWD)
        text = msg.as_string()
        server.sendmail(TOP_EMAIL, CC_EMAIL, text)

        logger.info (f"Email sent successfully!")
        server.quit()
    except Exception as e:
        logger.error(f"An error occurred: {e}")



# main
if __name__ == '__main__':

    # call function
    instances = list_ec2_instances()

    logger.info(f'generating csv report {FILE_NAME}')
    # generate report
    generate_csv_report(instances)

    logger.info(f'uploading report to s3')
    # upload report
    upload_report_to_s3()
    # send email
    send_email()
    # Thank message
    logger.info(f'Thank you for using this application!!!')
    logger.info(f"End of the log! \n" + "*" * 80)