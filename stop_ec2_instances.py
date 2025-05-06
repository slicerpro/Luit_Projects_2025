import boto3
import sys

ec2 = boto3.client('ec2')

for instance in range(4):
    ec2.create_instance()

response = ec2.list_instances()
print(response)


