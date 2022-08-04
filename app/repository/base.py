from multiprocessing.sharedctypes import Value
from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource

class BaseRepository:
    def __init__(self,
            db: ServiceResource,
            table_name: str,
            hash_key_name: str,
            range_key_name: str = None
            ) -> None:
        self._db = db
        self.table_name = table_name
        self.hash_key_name = hash_key_name
        self.range_key_name = range_key_name

    def get_all(self):
        table = self._get_table()
        response = table.scan()
        return response.get('Items', [])

    def get(self, hash_key: str, range_key: str = None):
        """Get item from dynamodb"""
        key = self._get_key(hash_key, range_key)
        try:
            table = self._get_table()
            response = table.get_item(Key=key)
            return response['Item']
        except ClientError as e:
            raise ValueError(e.response['Error']['Message'])

    def create(self, data: dict):
        """Create new item in dynamodb. Return new object."""
        table = self._get_table()
        response = table.put_item(Item=data)
        return data

    def update(self, hash_key: str, data: dict, range_key: str = None):
        """Update item in dynamodb. Return new object."""
        table = self._get_table()
        key = self._get_key(hash_key, range_key)
        update_expression = 'SET {}'.format(','.join(f'#{k}=:{k}' for k in data.keys()))
        expression_attribute_values = {f':{k}': v for k, v in data.items()}
        expression_attribute_names = {f'#{k}': k for k in data.keys()}
        response = table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames=expression_attribute_names,
            ReturnValues='ALL_NEW'
        )
        return response['Attributes']

    def delete(self, hash_key: str, range_key: str = None):
        """Delete item in dynamodb"""
        table = self._get_table()
        response = table.delete_item(
            Key=self._get_key(hash_key, range_key)
        )
        return None  # TODO: decide what to return here

    def _get_table(self):
        return self._db.Table(self.table_name)

    def _get_key(self, hash_key, range_key):
        key = { self.hash_key_name: hash_key }
        if range_key:
            key[self.range_key_name] = range_key
        return key
