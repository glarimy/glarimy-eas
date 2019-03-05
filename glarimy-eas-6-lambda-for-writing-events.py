import json
import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    iotevent = json.loads(event['body'])
        
    print(iotevent)
    table = dynamodb.Table("eas-events")
    table.put_item(Item=iotevent);
    
    return {
        'statusCode': 201,
        'body': json.dumps(iotevent)
    }
