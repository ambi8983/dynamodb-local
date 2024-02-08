import boto3

# Set the endpoint URL for DynamoDB Local
dynamodb_endpoint = "http://localhost:8000"

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb', endpoint_url=dynamodb_endpoint)


def display_table_structure(table_name):
    try:
        # Describe the table
        response = dynamodb.describe_table(TableName=table_name)

        # Extract and display table attributes
        table_description = response['Table']
        print(f"Table Name: {table_description['TableName']}")
        print(f"Attribute Definitions: {table_description['AttributeDefinitions']}")
        print(f"Key Schema: {table_description['KeySchema']}")
        print(f"Provisioned Throughput: {table_description['ProvisionedThroughput']}")
        print(f"Table Size Bytes: {table_description['TableSizeBytes']}")
        print(f"Table Status: {table_description['TableStatus']}")

    except dynamodb.exceptions.ResourceNotFoundException:
        print(f"Table '{table_name}' not found.")


if __name__ == "__main__":
    # Specify the table name you want to describe
    table_name_to_describe = "students"

    # Call the function to display table structure
    display_table_structure(table_name_to_describe)
