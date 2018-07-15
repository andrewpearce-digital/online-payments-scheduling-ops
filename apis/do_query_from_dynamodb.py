from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
import argparse

parser = argparse.ArgumentParser(description='Looks up online LPA Transaction ID from gov.uk pay.')
parser.add_argument('transaction_id', metavar='Transaction ID', type=str, help='a transaction id of LPA.')
args = parser.parse_args()

transaction_id = args.transaction_id

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource("dynamodb", region_name='eu-west-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table('ReceivedTransactionIDs')

print("Looking for Transaction ID " + transaction_id)

response = table.query(
    KeyConditionExpression=Key('transaction_id').eq(transaction_id)
)

for i in response['Items']:
    print(i['transaction_id'], ":", i['date_of_receipt'])
