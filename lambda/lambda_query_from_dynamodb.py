from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    transaction_id = event['full_transaction_id']

    if transaction_id is not None:
        print("looking for transaction id")
        
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        table = dynamodb.Table('ops_lambda_db')
        response = table.query(
            KeyConditionExpression=Key('transaction_id').eq(transaction_id)
            )

        db_write_response = json.dumps(response, indent=4, cls=DecimalEncoder)
        return db_write_response
    else:
        print("request failed - no transaction id provided")
        db_write_response = json.dumps(response, indent=4, cls=DecimalEncoder)
        return db_write_response