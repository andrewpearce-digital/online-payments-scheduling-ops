# This function makes a search and can return multiple results.
# The only filter for results is the transaction ID.

import json
import requests

def lambda_handler(event, context):
#TODO pass in value from api
    transaction_id = "12345"
    # make sure transaction_id value exists
    if transaction_id is not None:
        # Feedback
        print("looking up transaction id " + transaction_id)

        transaction_info = get_transaction_info(transaction_id)
        if transaction_info is not None:
            for results in transaction_info['results']:
                description = results['description']
                full_transaction_id = results['reference']
                amount_paid = results['amount']
                created_date = results['created_date']
                status = results['state']['status']
                refunded = results['refund_summary']['amount_available'] - amount_paid
                results_data = {
                    "description":description,
                    "full_transaction_id":full_transaction_id,
                    "amount_paid":amount_paid,
                    "created_date":created_date,
                    "status":status,
                    "refunded":refunded
                }
                results_data_json = json.dumps(results_data)
                print(results_data_json)
            return results_data_json
            # return transaction_info
        else:
            print("request failed - no results retrieved")
    else:
        print("request failed - no transaction id provided")
    return None

#TODO Provide the API key securely
#WARNING The key file is no longer being closed
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
        print('[!] [{0}] Invalid parameters. See Public API documentation for the correct data formats'.format(response.status_code))
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