# This function makes a search and can return multiple results.
# The only filter for results is the transaction ID.

import json
import requests
import argparse

# Pass arguments from command line
parser = argparse.ArgumentParser(description='Looks up online LPA Transaction ID from gov.uk pay.')
parser.add_argument('transaction_id', metavar='Transaction ID', type=str, help='a transaction id to look up.')
args = parser.parse_args()

# Feedback
print("! do_get_transactions")
print("looking up transaction id " + args.transaction_id)

# Read API key from file (excluded from repo)
with open(".key", "r") as key_file:
    api_token  = key_file.read()

api_url_base = 'https://publicapi.payments.service.gov.uk/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

# Make API call and handle errors
def get_transaction_info(transaction_id):

    api_url = '{0}v1/payments?reference='.format(api_url_base) + str(transaction_id)

    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 422:
        print('[!] [{0}] Invalid parameters: from_date, to_date, status, display_size. See Public API documentation for the correct data formats'.format(response.status_code))
        return None  
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None  
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None

# Print API Call Results
transaction_info = get_transaction_info(args.transaction_id)
if transaction_info is not None:
    print("Results: ")
    # print(json.dumps(transaction_info, indent=4, sort_keys=True))
    for results in transaction_info['results']:
        description = results['description']
        transaction_id = results['reference']
        amount_paid = results['amount']
        created_date = results['created_date']
        status = results['state']['status']
        refunded = results['refund_summary']['amount_available'] - amount_paid

        print("Order Description: " + (description))
        print("Transaction ID: " + str(transaction_id))
        print("Amount Paid: " + str(amount_paid))
        print("Date/Time Paid: " + created_date)
        print("Status: " + status)
        print("Amount Refunded: " + str(refunded))
        print("\n")
else:
    print('[!] Request Failed')
key_file.close()
print("! end of do_get_transactions")