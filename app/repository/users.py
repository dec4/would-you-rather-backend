from app.repository.base import BaseRepository
from app.db import ddb_client
from app.config import config

class UsersRepository(BaseRepository):
    def __init__(self):
        super().__init__(
            db=ddb_client,
            table_name=config.USERS_TABLE,
            hash_key_name='id'
        )

    def get_user(self, id: str):
        return self.get(id)

    def create_user(self, user: dict):
        return self.create(user)

    def update_user(self, user: dict):
        id = user.get('id')
        user.pop('id')
        return self.update(id, user)

    def delete_user(self, id: str):
        return self.delete(id)


users_repository = UsersRepository()
