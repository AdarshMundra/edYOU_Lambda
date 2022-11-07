import json
# import botocore
# from botocore.exceptions import ClientError
import codecs
from boto3 import Session
from boto3 import resource
import boto3

def lambda_handler(event, context):
    session = Session(region_name="us-west-2")
    polly = session.client("polly")
    
    s3 = resource('s3')
    bucket_name = "pollydemo2022"
    bucket = s3.Bucket(bucket_name)
    
    filename = "demo/mynameis.mp3"
    myText = """
    Hello,
    My name is Eralper.
    Welcome to my website kodyaz.com
    """
    
    response = polly.synthesize_speech(
    Text=myText,
    OutputFormat="mp3",
    VoiceId="Matthew")
    stream = response["AudioStream"]
    
    bucket.put_object(Key=filename, Body=stream.read())
    data = "https://pollydemo2022.s3.us-west-2.amazonaws.com/"+filename
    
    return{
        'data':data
    }    
    
    