import boto3

ec2 = boto3.resource('ec2')

#Locate running instances and delete them
instances = ec2.instances.filter(
    Filters = [{'Name': 'instance-state-name', 'Values': ['running']},
    {'Name':'tag:Environment', 'Values':['Development']}]
)
for instance in instances:
    print(instance.id, instance.state['Name'])
    try:
        instance.stop()
        print(f"Stopping instance: {instance.id}")
    
    except Exception as e:
        print(f"Error stopping instance {instance.id}: {e}")
    

#print(instances)
#for instance in instances:
#    try:
#        instance[InstanceId].stop()
#        print(f"Stopping instance: {instance}")
    
#    except Exception as e:
#        print(f"Error stopping instance {instance}: {e}")
        
