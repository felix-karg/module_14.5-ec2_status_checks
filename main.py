import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="eu-west-3")
ec2_resource = boto3.resource('ec2', region_name="eu-west-3")

def check_instance_status():
    reservations = ec2_client.describe_instances()
    for reservation in reservations['Reservations']:
        instances = reservation['Instances']
        for instance in instances:
            print(f"Status of instance {instance['InstanceId']} is {instance['State']['Name']}")

schedule.every(5).minutes.do(check_instance_status)

while True:
    schedule.run_pending()