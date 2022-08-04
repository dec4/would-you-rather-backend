from datetime import datetime
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator
from typing import List
from typing import Optional

class VotingOption(BaseModel):
    votes: Optional[List[str]] = []
    text: str

class Question(BaseModel):
    id: Optional[str] = None
    author: Optional[str]
    timestamp: Optional[datetime]
    optionOne: Optional[VotingOption]
    optionTwo: Optional[VotingOption]

    @validator("timestamp")
    def datetime_to_string(cls, v):
        return v.isoformat()

class CreateQuestionSchema(Question):
    author: str
    timestamp: Optional[datetime] = datetime.now().isoformat()
    optionOne: VotingOption
    optionTwo: VotingOption

class UpdateQuestionSchema(Question):
    id: str
