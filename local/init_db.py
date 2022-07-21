import boto3


DYNAMODB_URL='http://localhost:8000'
# NOTE: the following variables should match those in app/config.py:LocalConfig
AWS_ACCESS_KEY_ID='example'
AWS_SECRET_ACCESS_KEY='example'
REGION_NAME='us-west-2'
USERS_TABLE='wyr-users'
QUESTIONS_TABLE='wyr-questions'

def generate_wyr_tables(ddb):
    ddb.create_table(
        TableName=USERS_TABLE,
        AttributeDefinitions=[
            { 'AttributeName': 'id', 'AttributeType': 'S' },
        ],
        KeySchema=[
            { 'AttributeName': 'id', 'KeyType': 'HASH' },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )
    print(f'Successfully created table {USERS_TABLE}')

    ddb.create_table(
        TableName=QUESTIONS_TABLE,
        AttributeDefinitions=[
            { 'AttributeName': 'id', 'AttributeType': 'S' },
        ],
        KeySchema=[
            { 'AttributeName': 'id', 'KeyType': 'HASH' },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )
    print(f'Successfully created table {QUESTIONS_TABLE}')

def load_local_data(ddb):
    pass


if __name__  == '__main__':
    ddb = boto3.resource('dynamodb',
        endpoint_url=DYNAMODB_URL,
        region_name=REGION_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        use_ssl=False
    )
    generate_wyr_tables(ddb)
    load_local_data(ddb)
