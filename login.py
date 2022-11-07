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
user=dynamodb.Table('user')
Token_Data = dynamodb.Table('Token')

    
def lambda_handler(event, context):
    res=checkemail(event['email'])
    if(res['found']):
        data=res['data']
        role=res['role']
        Createddate = strftime("%Y-%m-%d", gmtime())
        Begindate = datetime.strptime(Createddate, "%Y-%m-%d")
        Enddate = Begindate + timedelta(days=10)
        Enddate = str(Enddate).split(" ")[0]
        if role == 'admin':
            if event['password']==data['password']:
                if event['device']=='mobile':
                    token = secrets.token_urlsafe(20)
                    user_id = data['id']
                    data1={
                        'token':token,
                        'created_at':Createddate,
                        'expired_at':Enddate,
                        'id':user_id
                    }
                    Token_Data.put_item(Item=data1)
                    return {'statusCode': 200,'body': 'Logged in','data': data,'Token':token}
                else:
                    token = secrets.token_urlsafe(20)
                    user_id = data['id']
                    data1={
                        'token':token,
                        'created_at':Createddate,
                        'expired_at':Enddate,
                        'id':user_id
                    }
                    Token_Data.put_item(Item=data1)
                    return {'statusCode': 200,'body': 'Logged in','data': data,'Token':token}
            else:
                return {'statusCode': 401,'body':'Password is incorrect'}
        elif role == 'executiveAdmin':
            if event['password']==data['password']:
                if event['device']=='mobile':
                    token = secrets.token_urlsafe(20)
                    user_id = data['id']
                    data1={
                        'token':token,
                        'created_at':Createddate,
                        'expired_at':Enddate,
                        'id':user_id
                    }
                    Token_Data.put_item(Item=data1)
                    return {'statusCode': 200,'body': 'Logged in','data': data,'Token':token}
                else:
                    token = secrets.token_urlsafe(20)
                    user_id = data['id']
                    data1={
                        'token':token,
                        'created_at':Createddate,
                        'expired_at':Enddate,
                        'id':user_id
                    }
                    Token_Data.put_item(Item=data1)
                    return {'statusCode': 200,'body': 'Logged in','data': data,'Token':token}
            else:
                return {'statusCode': 401,'body':'Password is incorrect'}
        
        else:
            if event['password']==data['password']:
                if event['device']=='mobile':
                    token = secrets.token_urlsafe(20)
                    user_id = data['id']
                    data1={
                        'token':token,
                        'created_at':Createddate,
                        'expired_at':Enddate,
                        'id':user_id
                    }
                    Token_Data.put_item(Item=data1)
                    return {'statusCode': 200,'body': 'Logged in','data': data,'Token':token}
                else:
                    token = secrets.token_urlsafe(20)
                    user_id = data['id']
                    data1={
                        'token':token,
                        'created_at':Createddate,
                        'expired_at':Enddate,
                        'id':user_id
                    }
                    Token_Data.put_item(Item=data1)
                    return {'statusCode': 200,'body': 'Logged in','data': data,'Token':token}
            
            else:
                return {'statusCode': 401,'body':'Password is incorrect'}
        
                
    else:
        return{
            'body':'No email found',
            'statusCode':402
        }
    
    
def checkemail(email):
    email=email.lower()
    data2 =user.get_item(Key={'email':email})
    if 'Item' in data2:
        if data2['Item']['role']=='admin':
            data={
                'found':True,
                'data':data2['Item'],
                'role':'admin'    
            }
        elif data2['Item']['role']=='executiveAdmin':
            data={
                'found':True,
                'data':data2['Item'],
                'role':'executiveAdmin'    
            }
        else:
            data={
                'found':True,
                'data':data2['Item'],
                'role':'user'    
            }
    else:
        data={
            'found':False
        }
    return data
