import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    table = dynamodb.Table("eas-events")
    response = table.scan();
    iotevents = response['Items']
    print (iotevents)

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials" : 'true'
         },
        'body': json.dumps(iotevents)
    } 
