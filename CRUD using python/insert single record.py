import boto3

# Set up DynamoDB client for DynamoDB Local
dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

# Define the table name
table_name = 'students'


def create_table():
    # Create the "students" table if it doesn't exist
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'},
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'},
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
    )


def insert_record():
    # Insert a record into the "students" table
    dynamodb.put_item(
        TableName=table_name,
        Item={
            'id': {'S': '1'},
            'name': {'S': 'RAM'}
        }
    )


def display_table_data():
    # Scan the table and display all records
    response = dynamodb.scan(TableName=table_name)
    items = response.get('Items', [])

    if not items:
        print("No records found in the table.")
    else:
        print("Table data:")
        for item in items:
            print(item)


if __name__ == "__main__":
    # Create table if it doesn't exist
    # create_table()

    # Insert record into the table
    insert_record()

    # Display table data
    display_table_data()
