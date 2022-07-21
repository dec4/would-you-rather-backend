import boto3
from boto3.resources.base import ServiceResource

from .config import config

def initialize_db() -> ServiceResource:
    ddb = boto3.resource('dynamodb',
        endpoint_url=config.DYNAMODB_URL,
        region_name=config.REGION_NAME,
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        use_ssl=(not config.APP_ENV == 'local'))
    return ddb

ddb_client = initialize_db()
