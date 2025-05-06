import boto3

ec2 = boto3.client('ec2')

instance_list = ec2.describe_instances()

for instance in instance_list['Reservations']:
    for i in instance['Instances']:
        print(i['InstanceId'])
        ec2.create_tags(
            Resources=[i['InstanceId']],
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': 'Development'
                }
            ]
        )