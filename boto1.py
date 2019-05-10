import boto3
import datetime
import time
# Solution for the 1 st and 2nd one 
# Create IAM client

#1) Write a boto3 script to retrieve access key age of a user, please take username as an input.
#2) Write a boto3 script to disable access keys if access key age greater than 100 days.

iam = boto3.client('iam')

username = input('enter username to be verified')
res = iam.list_access_keys(UserName=username)
print(res)
accesskeydate=res['AccessKeyMetadata'][0]['CreateDate']
accesskeydate = accesskeydate.strftime("%Y-%m-%d %H:%M:%S")
currentdate = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

accesskeyd = time.mktime(datetime.datetime.strptime(accesskeydate, "%Y-%m-%d %H:%M:%S").timetuple())
currentd = time.mktime(datetime.datetime.strptime(currentdate, "%Y-%m-%d %H:%M:%S").timetuple())

active_days = (currentd - accesskeyd)/60/60/24 ### We get the data in seconds. converting it to days
print (int(round(active_days)))

if active_days>=100:
    response = access_key.deactivate()
else :
    print("Access key is activated")






# Get last use of access key
# response = iam.get_access_key_last_used(
#     AccessKeyId='AKIAQAQEAS4WFUGWGEGF'
# )

# print(response['AccessKeyLastUsed'])