from uuid import uuid4

from app.schemas.users import CreateUserSchema
from app.schemas.users import UpdateUserSchema
from app.repository.users import users_repository


class UsersDomain():
    def __init__(self, repository) -> None:
        self._repository = repository

    def get_all_users(self):
        return self._repository.get_all()

    def get_user(self, id: str):
        return self._repository.get_user(id)

    def create_user(self, user: CreateUserSchema):
        if not user.id:
            user.id = str(uuid4())
        return self._repository.create_user(user.dict())

    def update_user(self, user: UpdateUserSchema):
        return self._repository.update_user(user.dict(exclude_unset=True))

    def delete_user(self, id: str):
        return self._repository.delete_user(id)


users_domain = UsersDomain(users_repository)
