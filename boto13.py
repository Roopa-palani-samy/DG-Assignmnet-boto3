import boto3

client = boto3.client('ec2')
print(client)
# 3)Tagging owner id because user name is tagged by default 
response = client.describe_instances(
    Filters=[
        {
            'Name': 'owner-id',
            'Values': [
                '001082169132',
            ]
        },
    ]
)

owner_id = '001082169132'
res = client.create_tags(
    
    Resources=[
        'i-0efb5fdb52b2ff78b',
    ],
    Tags=[
        {
            'Key': 'ownername',
            'Value': owner_id
        },
    ]
)
print(res)