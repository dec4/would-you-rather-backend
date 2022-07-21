from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from pydantic.types import UUID4
from typing import List
from typing import Optional
from uuid import uuid4

from app.repository.users import UsersRepository
from app.repository.users import users_repository


class OptionEnum(str, Enum):
    OPTION_ONE = 'optionOne'
    OPTION_TWO = 'optionTwo'

class UsersModel(BaseModel):
    id: Optional[str] = None
    name: str = Field(..., example='John Doe')
    avatarURL: Optional[str] = Field(..., example='https://picsum.photos/200')
    questions: Optional[List[str]] = []
    answers: Optional[dict[str, OptionEnum]] = {}


class UsersDomain():
    def __init__(self, repository) -> None:
        self._repository = repository

    def get_all_users(self):
        return self._repository.get_all()

    def get_user(self, id: str):
        return self._repository.get_user(id)

    def create_user(self, user: UsersModel):
        if not user.id:
            user.id = str(uuid4())
        return self._repository.create_user(user.dict())

    def update_user(self, user: UsersModel):
        return self._repository.update_user(user.dict())

    def delete_user(self, id: str):
        return self._repository.delete_user(id)


users_domain = UsersDomain(users_repository)
