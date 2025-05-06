import boto3
import sys

ec2 = boto3.client('ec2')
instance = boto3.resource('ec2', region_name='us-east-1')

created_instances = instance.create_instances(
    ImageId = "ami-0f88e80871fd81e91",
    KeyName = "Lin_01_key",
    InstanceType = "t2.micro",
    MaxCount = 4,
    MinCount = 4,
    SecurityGroupIds = ["sg-00a561190de9ecda2"],
)
instance_ids = []
for instance in created_instances:
    instance_ids.append(instance.id)
print(instance_ids)




