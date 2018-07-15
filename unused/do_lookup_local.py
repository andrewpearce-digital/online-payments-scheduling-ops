import argparse

# Pass arguments from command line
parser = argparse.ArgumentParser(description='Looks up online LPA Transaction ID from gov.uk pay.')
parser.add_argument('transaction_id', metavar='Transaction ID', type=str, help='a transaction id to look up.')
args = parser.parse_args()
transaction_id = args.transaction_id
# Feedback
# print("! do_lookup_local")
print("looking up transaction id " + args.transaction_id + " locally...")

# read back .mockdb to see if it's been written correctly
file = open(".mockdb","r")

# repeat for each line  in .mockdb
for line in file:
  
  # split each line into an array called "fields" using the "," as a separator:
  fields = line.split(",")
  
  #and let's extract the data:
  read_transaction_id = fields[0]
  read_date_of_receipt = fields[1]
  read_last_updated = fields[2]
  
  # print the records
if read_transaction_id == transaction_id:
    print("found local - already received \n")
    print(read_transaction_id + "\n   Received on " + read_date_of_receipt + ":\n   Last Updated: " + read_last_updated)
else:
    print("not yet received, will do_get_transactions instead... \n")
    import do_get_transactions

file.close()
