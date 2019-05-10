#Write a boto3 script to tag an EC2 instance with the username who launched it.
#Write a Lambda function for #3, trigger function only when an EC2 instance is created.


import json
import boto3
import logging 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    logging.info(str(event))
    
    instance_id = event['instance-id']

    response = ec2.describe_instances(InstanceIds = [instance_id])
    print str(response)
    owner_id = response['Reservations'][0]['OwnerId']
    print str(owner_id)
    res = client.create_tags(
    Resources=[
        instance_id,
    ],
    Tags=[
        {
            'Key': 'ownername',
            'Value': owner_id
        },
    ])
    print(res)
