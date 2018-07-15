user enters `transaction_id`
lookup id on pay
return full `transaction_id`
query full `transaction_id` on dynamodb to see if it's already received

if not received
    allow user to provide a `date_of_receipt`
    write full `transaction_id` and `date_of_receipt` to dynamodb
if received 
    do not allow user to write to entry to dynamodb

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.04.html