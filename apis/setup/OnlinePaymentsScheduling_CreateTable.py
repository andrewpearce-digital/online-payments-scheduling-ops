from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='ReceivedTransactionIDs',
    KeySchema=[
        {
            'AttributeName': 'transaction_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'date_of_receipt',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'transaction_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'date_of_receipt',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
