# online-payments-scheduling-ops
A web application to schedule online payments

This is not intended to be used by anyone else at this time.

This project is me learning while doing.

activate the env
```sh
source apis/bin/activate
```
| Script                    | Description                                                      |
|---------------------------|------------------------------------------------------------------|
|do_get_transactions.py     | calls gov.uk pay api to search a reference, returns data         |
|do_query_from_dynamodb.py  | looks up reference from dynamodb for references already received |
|do_write_to_dynamodb.py    | writes a reference, date of receipt and update time to dynamodb  |
|process_flow.md            | just a note about the flow I'm trying to acheive                 |
