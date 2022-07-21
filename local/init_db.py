import boto3
import os, json


DYNAMODB_URL='http://localhost:8000'
# NOTE: the following variables should match those in app/config.py:LocalConfig
AWS_ACCESS_KEY_ID='example'
AWS_SECRET_ACCESS_KEY='example'
REGION_NAME='us-west-2'
USERS_TABLE='wyr-users'
QUESTIONS_TABLE='wyr-questions'

def generate_wyr_tables(ddb):
    try:
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
    except Exception as e:  # todo: properly import ResourceInUseException
        print(e)

    try:
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
    except Exception as e:  # todo: properly import ResourceInUseException
        print(e)

def load_local_data(ddb, folder_path):
    json_files = [pos_json for pos_json in os.listdir(folder_path) if pos_json.endswith('.json')]
    for file_name in json_files:
        with open(folder_path + file_name, 'r') as f:
            data = json.load(f)
        table_name = file_name[:-len('.json')]  # strip .json
        table = ddb.Table(table_name)
        for item in data.values():
            table.put_item(
                Item=item
            )
        print(f'Loaded data for table {table_name}')


if __name__  == '__main__':
    ddb = boto3.resource('dynamodb',
        endpoint_url=DYNAMODB_URL,
        region_name=REGION_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        use_ssl=False
    )
    generate_wyr_tables(ddb)
    load_local_data(ddb, './local_data/')
