import boto3

# Configure DynamoDB local endpoint (assuming it's running locally on default port 8000)
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Specify the table name
table_name = 'students'

# Get the DynamoDB table
table = dynamodb.Table(table_name)

# Scan the table to fetch all items
response = table.scan()

# Display the table data
items = response.get('Items', [])
if not items:
    print(f"No items found in the {table_name} table.")
else:
    print(f"Table data for {table_name}:")
    for item in items:
        print(item)
