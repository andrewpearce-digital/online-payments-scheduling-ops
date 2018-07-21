from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    transaction_id = event['full_transaction_id']

    if transaction_id is not None:
        print("looking for transaction id")
        
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        table = dynamodb.Table('ops_lambda_db')
        response = table.query(
            KeyConditionExpression=Key('transaction_id').eq(transaction_id)
            )

        if response['Count'] > 0:
            print("match found!")
            return response
        else:
            print("no matches found")
            return None
    else:
        print("request failed - no transaction id provided")
        return None