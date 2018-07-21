from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from datetime import datetime

def lambda_handler(event, context):
    transaction_id = event['full_transaction_id']
    date_of_receipt = event['date_of_receipt']

    if transaction_id and date_of_receipt is not None:
        # Feedback
        print("writing transaction to database")

        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        table = dynamodb.Table('ops_lambda_db')
        response = table.put_item(
        Item={
                'date_of_receipt': date_of_receipt,
                'transaction_id': transaction_id,
                'last_updated': str(datetime.now())
            }
        )
        return response
    else:
        print("request failed - no transaction id provided or no date of receipt provided")
        return None
