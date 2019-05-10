import boto3

client = boto3.client('ec2')
# classic_address = ec2.ClassicAddress('public_ip')
# print(classic_address)

response = client.describe_instances(
    InstanceIds=[
        'i-0efb5fdb52b2ff78b',
    ]
)

# response = client.describe_instance_attribute(
#     Attribute='PublicIp',
#     InstanceId='i-0efb5fdb52b2ff78b'
# )
# print(response)
print('***********************************************')
if response['Reservations'][0]['Instances'][0]['PublicIpAddress'] :
    print(response['Reservations'][0]['Instances'][0]['PublicIpAddress'])
    res = client.stop_instances(
    InstanceIds=[
        'i-0efb5fdb52b2ff78b',
    ],)
    print(res)