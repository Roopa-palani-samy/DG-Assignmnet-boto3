import boto3
ec2 = boto3.resource('ec2')
ids = ['i-0efb5fdb52b2ff78b']            #specific instance of ec2
instance = ec2.instances.filter(InstanceIds=ids)
sg_id = ['sg-00c0f70ca38079b4a']   #security group id 
# print(instance.id, instance.instance_type)
instance.modify_attribute(Groups=sg_id)