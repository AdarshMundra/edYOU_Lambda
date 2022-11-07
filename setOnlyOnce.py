import json
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')
user=dynamodb.Table('user')

def lambda_handler(event, context):
    unique = event['id'].lower()
    resp = user.get_item(Key={'email': unique})
    l=resp['Item']
    Timeout_id=l['Timeout_id']
    if Timeout_id !='':
        return {
            'statusCode': 200,
            'body': 'Your new password has been set.'
            }    
    else:
        return {
            'statusCode': 410,
            'body': 'Password set once please used forgot password.'
            }
            

