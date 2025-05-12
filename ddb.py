import boto3

client = boto3.client('dynamodb')

CreateResponse = client.create_table(
    AttributeDefinitions=[
        {
            "AttributeName": "pet_species",
            "AttributeType" : "S"
        },
        {
            "AttributeName": "pet_Id",
            "AttributeType": "N"
        }
    ],
    KeySchema=[
        {
            "AttributeName": "pet_species",
            "KeyType": "HASH"
        },
        {
            "AttributeName": "pet_Id",
            "KeyType": "RANGE"
        },

    ],
BillingMode = "PAY_PER_REQUEST",
TableName = "PetInventory"
)
# print the response
print("Table Created\n")
print(CreateResponse)