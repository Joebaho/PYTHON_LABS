'''
AWS CODE: cost_reporting.py

Write a program that will Cost Reporting: 
Use AWS Cost Explorer API with Boto3 to retrieve and generate a cost report for AWS resources.
'''
import boto3
from datetime import datetime, timedelta
import csv

def get_cost_and_usage(start_date, end_date):
    """
    Retrieve cost and usage data from AWS Cost Explorer
    """
    client = boto3.client('ce', region_name='us-east-1')
    
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date,
            'End': end_date
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[
            {'Type': 'DIMENSION', 'Key': 'SERVICE'}
        ]
    )
    
    return response['ResultsByTime']

def generate_cost_report(months=6):
    """
    Generate a cost report for the specified number of months
    """
    end_date = datetime.now().replace(day=1).strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30*months)).replace(day=1).strftime('%Y-%m-%d')
    
    print(f"Generating cost report from {start_date} to {end_date}")
    
    results = get_cost_and_usage(start_date, end_date)
    
    # Prepare CSV file
    csv_filename = 'aws_cost_report.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Month', 'Service', 'Cost (USD)'])
        
        total_cost = 0
        for result in results:
            month = result['TimePeriod']['Start']
            for group in result['Groups']:
                service = group['Keys'][0]
                cost = float(group['Metrics']['UnblendedCost']['Amount'])
                total_cost += cost
                writer.writerow([month, service, f"{cost:.2f}"])
        
        writer.writerow(['', 'Total', f"{total_cost:.2f}"])
    
    print(f"Cost report generated: {csv_filename}")
    print(f"Total cost for the period: ${total_cost:.2f}")

if __name__ == "__main__":
    generate_cost_report(months=6)