from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from typing import List
from typing import Optional


class OptionEnum(str, Enum):
    OPTION_ONE = 'optionOne'
    OPTION_TWO = 'optionTwo'

class User(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = Field(example='John Doe')
    avatarURL: Optional[str] = Field(example='https://picsum.photos/200')
    questions: Optional[List[str]]
    answers: Optional[dict[str, OptionEnum]]

# Below are fine grained schemas marking initializations/requirements as needed:

class CreateUserSchema(User):
    name: str
    questions: Optional[List[str]] = []
    answers: Optional[dict[str, OptionEnum]] = {}

class UpdateUserSchema(User):
    id: str
