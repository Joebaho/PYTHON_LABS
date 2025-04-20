import boto3
import botocore
import csv
import logging

# Setup loggers
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# global var
REPORT_NAME = 'ec2_report.csv'

def list_all_ec2_instances():
    """
    Gather all ec2 instance
    :param
    :return
    """
    # create an empty list
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
            instance_name = instance["Tags"][0]['Value'] 
            instance_type = instance["InstanceType"]
            image_id = instance["ImageId"]
            state = instance["State"]["Name"]

            # Add all element to the list
            list_ec2_instances.update({'instance_name': [instance_name], 'instance_type': [instance_type], 'image_id': [image_id], 'state': [state]})

    return list_ec2_instances

def generate_csv_report(instances):
    """
        This function will generate a csv report per Micheal
        :param list of instances
        :return return true if valid
    """
    try:
        with open(REPORT_NAME, 'w', newline='') as csvfile:
            fieldnames = ['instance_name', 'instance_type', 'image_id', 'state']
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fieldnames)
            csvwriter.writerows(instances)
    except OSError as error:
        logger.error(f"Laura said file wasn't found! {error}")
        return False
    return True # optional

def upload_report_to_s3():
    """
        This function will upload csv report to s3 bucket
        :param 
        :return 
    """
    
    s3_client = boto3.client('s3')

    try:
        s3_client.upload_file(REPORT_NAME, 'i-love-eating-fufu-with-spicy-goat-meat', REPORT_NAME)
    except botocore.exceptions.ClientError as error:
        logger.error(f"Something happened while uploading the file {error}")


# main
if __name__ == '__main__':

    # call function
    instances = list_all_ec2_instances()

    logger.info(f'generating csv report {REPORT_NAME}')
    # generate report
    generate_csv_report(instances)

    logger.info(f'uploading report to s3')
    # upload report
    upload_report_to_s3()

    logger.info(f'Good night folks!!!')