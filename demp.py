import json
import json
import codecs
from boto3 import Session
from boto3 import resource
import boto3
import urllib3
http = urllib3.PoolManager()
from decimal import Decimal

def lambda_handler(event, context):
    url="http://34.221.203.186:5002/webhooks/rest/webhook"
    encoded_data = json.dumps({  "sender": "adarsh","message": event['message']})
    resp = http.request('POST',url,body=encoded_data,headers={'Content-Type': 'application/json'})
    data=json.loads(resp.data.decode('utf-8'))
    data1=data[0]['text']
    if data1 in ['0','1','2','3','4']:
      data1=int(data1)
      description=event['description']
      data1=description[data1]
    else:
      pass
    
    session = Session(region_name="us-west-2")
    polly = session.client("polly")
    
    s3 = resource('s3')
    bucket_name = "pollydemo2022"
    bucket = s3.Bucket(bucket_name)
    
    filename = event['filename']
    myText = data1
    
    response = polly.synthesize_speech(
    Text=myText,
    OutputFormat="mp3",
    VoiceId="Matthew")
    stream = response["AudioStream"]
    
    bucket.put_object(Key=filename, Body=stream.read())
    data2 = "https://pollydemo2022.s3.us-west-2.amazonaws.com/"+filename
    
    
    return {
        'statusCode': 200,
        'body': data2
    }
