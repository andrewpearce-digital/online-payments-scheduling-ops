# once a record has been looked up,
# user mark as received
# at this point, record the transaction id and date of receipt to the .mockdb file.

import argparse
from datetime import datetime

# pass arguments from command line
parser = argparse.ArgumentParser(description='Looks up online LPA Transaction ID from gov.uk pay.')
parser.add_argument('transaction_id', metavar='Transaction ID', type=str, help='a transaction id of LPA.')
parser.add_argument('date_of_receipt', metavar='Date of Receipt', type=str, help='date the LPA was received in the office.')
args = parser.parse_args()
test = False

# feedback
print("Writing the following values...")
print("transaction id: " + args.transaction_id)
print("date of receipt: " + args.date_of_receipt)

# write values to the mock database .mockdb
with open(".mockdb", "a") as mockdb_file:
    mockdb_file.write(args.transaction_id + "," +args.date_of_receipt + "," + str(datetime.now()) + "\n")

if test == True:
    # read back .mockdb to see if it's been written correctly
    file = open(".mockdb","r")

    # repeat for each line  in .mockdb
    print("\n \n Reading back entries... \n")
    for line in file:

        # split each line into an array called "fields" using the "," as a separator:
        fields = line.split(",")

        #and let's extract the data:
        read_transaction_id = fields[0]
        read_date_of_receipt = fields[1]
        read_last_updated = fields[2]

        # print the records
        print(read_transaction_id + "\n   Received on " + read_date_of_receipt + ":\n   Last Updated: " + read_last_updated)
    
    file.close()
