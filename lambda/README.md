# online payments scheduling - lambdas

This folder contains lambda functions for a serverless online payment scheduling application.

an lpa is paid for online, and once received in the office is acknowledged.

| Function                   | Events                               | Description                                                                                     |
|----------------------------|------------------------------------------------------------------|---------------------------------------------------------------------|
|lambda_get_transactions     | `lpa_id`                                | calls gov.uk pay api to search a `lpa_id` and returns transaction data                       |
|lambda_query_from_dynamodb  | `full_transaction_id`                   | looks up `full_transaction_id` from dynamodb for transactions already acknowledged           |
|lambda_write_to_dynamodb    | `full_transaction_id` `date_of_receipt` | writes a `full_transaction_id`, `date_of_receipt` and `last_updated` date andtime to dynamodb|
