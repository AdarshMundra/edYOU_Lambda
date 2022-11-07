import json
import boto3
from uuid import uuid4
import secrets
from boto3.dynamodb.conditions import Key
from time import gmtime, strftime
from datetime import timedelta
from datetime import datetime
import string
import random
import smtplib

dynamodb = boto3.resource('dynamodb')
Question=dynamodb.Table('Question')



def lambda_handler(event, context):
    data2 =Question.get_item(Key={'id':event['id']})
    if 'Item' in data2:
        return {
            'statusCode': 200,
            'body': data2['Item']
        }
    else:
        return {
            'statusCode': 200,
            'body': 'No data found'
        }
