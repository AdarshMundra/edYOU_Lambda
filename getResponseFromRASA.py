import json
import urllib3
http = urllib3.PoolManager()
from decimal import Decimal
def lambda_handler(event, context):
    url="http://34.221.203.186:5002/webhooks/rest/webhook"
    encoded_data = json.dumps({  "sender": "adarsh","message": event['message']})
    resp = http.request('POST',url,body=encoded_data,headers={'Content-Type': 'application/json'})
    data=json.loads(resp.data.decode('utf-8'))
    data1=data[0]['text']
    # TODO implement
    if data1 in ['0','1','2','3','4']:
      data1=int(data1)
      description=event['description']
      data1=description[data1]
    else:
      pass
    return {
        'statusCode': 200,
        'body': data1
    }
