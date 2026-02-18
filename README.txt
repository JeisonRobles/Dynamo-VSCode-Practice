# 🚀 DynamoDB VSCode Practice — Python + boto3 + IAM + Streams + Lambda + CloudWatch Logs

A hands-on AWS DynamoDB project built locally using **VSCode**, **Python**, **boto3**, and **IAM credentials**.
Adding a web interface check with CloudWatch Logs to see changes on the table.

This project demonstrates how to:

- Connect to AWS DynamoDB from a local machine
- Create a table programmatically
- Perform full CRUD operations


---

## 🧠 Learning Goals

This project was created to deeply understand:

- 🔐 IAM authentication (Access Keys + Credential Provider Chain)
- 🧩 DynamoDB data modeling (Partition Key + Sort Key)
- ⚡ Query vs GetItem
- 🔄 UpdateExpression & ConditionExpression
- 🗑 Safe Delete operations
- 🐍 boto3 SDK structure (client vs resource)

---

## 🏗 Architecture

Local Machine (VSCode)
│
│ boto3 SDK
│
▼
AWS DynamoDB (Cloud)

Authentication:
- IAM User (programmatic access)
- Configured locally using `aws configure`
- boto3 automatically reads credentials

## 📂 Project Structure
dynamodb-vscode-practice/
│
├── create_table.py # Creates DynamoDB table
├── app.py # Full CRUD operations
├── requirements.txt
├── .gitignore
└── README.md


---

## 🏛 DynamoDB Table Design

**Table Name:** `CustomerProducts`

| Attribute      | Type | Key Type |
|---------------|------|----------|
| customer_id   | String | Partition Key (HASH) |
| product_id    | String | Sort Key (RANGE) |

### Why this design?

This models a **one-to-many relationship**:


Example item:

```json
{
  "customer_id": "CUST-1001",
  "product_id": "SAV-01",
  "product_type": "savings",
  "balance": 1500
}

🔐 IAM Setup

Create IAM User
Enable programmatic access

Attach policy:
AmazonDynamoDBFullAccess (for practice)

Run locally:
aws configure


🛠 Installation

1️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate

2️⃣ Install dependencies
pip install boto3
pip freeze > requirements.txt

🏗 Create the Table
python create_table.py

Wait until the table becomes ACTIVE in AWS Console.

🚀 Run the App (CRUD Demo)
python app.py

The script demonstrates:

-Create item
-Read (Query + GetItem)
-Update attributes
-Delete item


🔄 CRUD Operations Implemented
-CREATE
-READ
-UPDATE
-DELETE

🧠 Key DynamoDB Concepts Demonstrated
Partition Key (HASH)

Determines how data is distributed across partitions.
Sort Key (RANGE)
Allows multiple items under the same partition key.

Query vs Scan

Query → Efficient (uses partition key)
Scan → Reads entire table (expensive)
This project uses Query.

PAY_PER_REQUEST

Billing mode is set to:
PAY_PER_REQUEST



🐍 What is boto3?

boto3 is the official AWS SDK for Python.

It allows Python applications to:
-Authenticate with AWS
-Send signed API requests
-Interact with cloud services
-Two interfaces:
-client → Low-level API
-resource → High-level object abstraction (used here)

🔒 Security Best Practices Followed

-No hardcoded credentials
-IAM authentication via aws configure
-Uses ConditionExpression to prevent unintended writes
-Principle of least privilege (recommended for production)

📚 Why This Project Matters

This repository demonstrates practical understanding of:

-AWS IAM
-NoSQL modeling
-Cloud authentication
-Python cloud integration
-Data engineering fundamentals
-It serves as a foundational step toward:
-AWS Data Engineering certification
-Serverless architectures (Lambda + DynamoDB)
-Replacing local SQLite with cloud storage
-Building scalable agent systems backed by DynamoDB

🔮 Possible Extensions

Add CLI interface

Add pagination handling

Add Global Secondary Index (GSI)

Replace IAM User with IAM Role

Deploy via AWS Lambda

Integrate with FastAPI backend

Add logging & error handling layer

👨‍💻 Author

Built as part of hands-on AWS Data Engineering practice.

📌 License

MIT


# Table Created:

![Table](img/Table.png)

# Lambda:

![Lambda](img/Lambda.png)

#  CloudWatch
![CloudWatch](img/CloudWatchLog.png)
