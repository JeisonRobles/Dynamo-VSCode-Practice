import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("CustomerProducts")

#CRUD OPERATIONS

# CREATE
def add_product(customer_id, product_id, product_type, balance):
    table.put_item(
        Item={
            "customer_id": customer_id,
            "product_id": product_id,
            "product_type": product_type,
            "balance": balance
        }
    )
    print("Product added.")


# READ
def get_customer_products(customer_id):
    response = table.query(
        KeyConditionExpression=Key("customer_id").eq(customer_id)
    )
    return response["Items"]

# DELETE
def delete_product(customer_id: str, product_id: str) -> None:
    """
    Delete an item.
    Uses ConditionExpression so it fails if the item doesn't exist (clean feedback).
    """
    try:
        table.delete_item(
            Key={"customer_id": customer_id, "product_id": product_id},
            ConditionExpression="attribute_exists(customer_id) AND attribute_exists(product_id)",
        )
        print(f"[DELETE] Deleted: {customer_id} / {product_id}")
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            print(f"[DELETE] Item does not exist: {customer_id} / {product_id}")
        else:
            raise

# UPDATE
def update_balance(customer_id: str, product_id: str, new_balance: float) -> None:
    """
    Update only the balance attribute.
    Uses ConditionExpression so it fails if the item doesn't exist (safer).
    """
    try:
        table.update_item(
            Key={"customer_id": customer_id, "product_id": product_id},
            UpdateExpression="SET balance = :b",
            ExpressionAttributeValues={":b": new_balance},
            ConditionExpression="attribute_exists(customer_id) AND attribute_exists(product_id)",
            ReturnValues="UPDATED_NEW",
        )
        print(f"[UPDATE] Balance updated: {customer_id} / {product_id} -> {new_balance}")
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            print(f"[UPDATE] Item does not exist: {customer_id} / {product_id}")
        else:
            raise

if __name__ == "__main__":
    add_product("CUST-1001", "SAV-01", "savings", 1500)
    add_product("CUST-1002", "SAV-02", "savings", 1300)
    add_product("CUST-1003", "SAV-01", "savings", 1500)
    add_product("CUST-1004", "SAV-02", "credit_card", 1000)
    delete_product("CUST-1002", "SAV-02")
    delete_product("CUST-1003", "SAV-01")
    update_balance("CUST-1001", "SAV-01",3000)
    products = get_customer_products("CUST-1001")
    print(products)