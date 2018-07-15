# test values
# 33512436750-1512039405 
# 01/05/2018

from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description='Looks up online LPA Transaction ID from gov.uk pay.')
parser.add_argument('transaction_id', metavar='Transaction ID', type=str, help='a transaction id of LPA.')
parser.add_argument('date_of_receipt', metavar='Date of Receipt', type=str, help='date the LPA was received in the office.')
args = parser.parse_args()

transaction_id = args.transaction_id
date_of_receipt = args.date_of_receipt

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table('ReceivedTransactionIDs')

response = table.put_item(
   Item={
        'date_of_receipt': date_of_receipt,
        'transaction_id': transaction_id,
        'last_updated': str(datetime.now())
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))