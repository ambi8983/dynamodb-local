import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

# Define the table schema
table_name = 'Test'
key_schema = [{'AttributeName': 'id', 'KeyType': 'HASH'}]
attribute_definitions = [{'AttributeName': 'id', 'AttributeType': 'N'}]

# Create the table
dynamodb.create_table(
    TableName=table_name,
    KeySchema=key_schema,
    AttributeDefinitions=attribute_definitions,
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait for the table to be created
dynamodb.get_waiter('table_exists').wait(TableName=table_name)

# Insert data into the table
data = [
    {'id': 1, 'name': 'John Doe', 'age': 25},
    {'id': 2, 'name': 'Jane Smith', 'age': 30},
    {'id': 3, 'name': 'Bob Johnson', 'age': 22}
]

for item in data:
    dynamodb.put_item(
        TableName=table_name,
        Item={
            'id': {'N': str(item['id'])},
            'name': {'S': item['name']},
            'age': {'N': str(item['age'])}
        }
    )

print(f"Data inserted into {table_name} table.")
