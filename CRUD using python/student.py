import boto3
from botocore.exceptions import NoCredentialsError

# Configure DynamoDB client for local development
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Define the table name
table_name = 'students'

# Create or get the 'students' table
try:
    table = dynamodb.create_table(
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
    table.wait_until_exists()
except dynamodb.meta.client.exceptions.ResourceInUseException:
    table = dynamodb.Table(table_name)

# Function to insert data into the table
def insert_data(name, student_id):
    try:
        table.put_item(Item={'name': name, 'id': student_id})
        print(f"Data inserted successfully: {{'name': '{name}', 'id': '{student_id}'}}")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Function to display all data from the table
def display_data():
    try:
        response = table.scan()
        items = response.get('Items', [])
        if not items:
            print("No data found in the table.")
        else:
            print("Table data:")
            for item in items:
                print(item)
    except Exception as e:
        print(f"Error displaying data: {e}")

# Insert data into the table
insert_data('RAM', '1')
insert_data('SAM', '2')
insert_data('SITA', '3')
insert_data('GITA', '4')
insert_data('RAMAN', '5')
insert_data('GOPAL', '6')

# Display data from the table
display_data()
