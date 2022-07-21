import os

def get_config():
    if os.environ.get('APP_ENV').lower() == 'local':
        return LocalConfig()
    else:
        raise Exception('Unknown App Env')

class LocalConfig():
    APP_ENV='local'
    DYNAMODB_URL='http://db:8000'
    AWS_ACCESS_KEY_ID='example'
    AWS_SECRET_ACCESS_KEY='example'
    REGION_NAME='us-west-2'
    USERS_TABLE='wyr-users'
    QUESTIONS_TABLE='wyr-questions'

config = get_config()
