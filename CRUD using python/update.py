import boto3

# Initialize a DynamoDB client (make sure to use the correct endpoint_url)
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Specify the table name
table_name = 'students'

# Get reference to the DynamoDB table
table = dynamodb.Table(table_name)


def update_student_data(student_id, new_name):
    try:
        # Update item in the table
        response = table.update_item(
            Key={'id': student_id},
            UpdateExpression='SET #n = :new_name',
            ExpressionAttributeNames={'#n': 'name'},
            ExpressionAttributeValues={':new_name': new_name},
            ReturnValues='UPDATED_NEW'
        )
        print("UpdateItem succeeded:", response)
    except Exception as e:
        print("Error updating item:", str(e))


def display_student_data(student_id):
    try:
        # Get item from the table
        response = table.get_item(
            Key={'id': student_id}
        )
        item = response.get('Item')
        if item:
            print("Student data:", item)
        else:
            print(f"Student with id {student_id} not found.")
    except Exception as e:
        print("Error getting item:", str(e))


# Example: Update and display data
student_id = '1'
new_name = 'RAM'

# Update data
update_student_data(student_id, new_name)

# Display updated data
display_student_data(student_id)
