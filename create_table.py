import boto3

dynamodb = boto3.client("dynamodb", region_name = "us-east-1")

def create_table():
    response = dynamodb.create_table(
        TableName="CustomerProducts",
        KeySchema=[
            {"AttributeName": "customer_id", "KeyType": "HASH"},
            {"AttributeName": "product_id", "KeyType": "RANGE"}
        ],
        AttributeDefinitions=[
            {"AttributeName": "customer_id", "AttributeType": "S"},
            {"AttributeName": "product_id", "AttributeType": "S"}
        ],
        BillingMode="PAY_PER_REQUEST"
    )
    print("Table creation initiated.")

if __name__ == "__main__":
    create_table()