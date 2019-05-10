import boto3

client = boto3.client('ec2')
response = client.describe_instances(
    InstanceIds=[
        'i-0efb5fdb52b2ff78b',
    ]
)
print('***********************************************')
if response['Reservations'][0]['Instances'][0]['PublicIpAddress'] :
    print(response['Reservations'][0]['Instances'][0]['PublicIpAddress'])
    res = client.stop_instances(
    InstanceIds=[
        'i-0efb5fdb52b2ff78b',
    ],)
    print(res)