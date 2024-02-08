import boto3

# Assuming DynamoDB Local is running on localhost:8000
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Specify the table name
table_name = 'students'

# Get reference to the table
table = dynamodb.Table(table_name)


def delete_record(student_id):
    try:
        # Delete the record with the specified ID
        response = table.delete_item(
            Key={
                'id': student_id
            }
        )
        print(f"Record with ID {student_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting record: {e}")


def display_table_data():
    try:
        # Scan the table to retrieve all records
        response = table.scan()
        items = response.get('Items', [])

        # Display table data
        if items:
            print("Table Data:")
            for item in items:
                print(item)
        else:
            print("Table is empty.")
    except Exception as e:
        print(f"Error displaying table data: {e}")


if __name__ == "__main__":
    # ID of the record to be deleted
    record_to_delete_id = '1'

    # Delete the record
    delete_record(record_to_delete_id)

    # Display the remaining table data
    display_table_data()
