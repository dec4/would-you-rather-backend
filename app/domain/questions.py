from uuid import uuid4

from app.repository.questions import questions_repository
from app.schemas.questions import CreateQuestionSchema
from app.schemas.questions import UpdateQuestionSchema

class QuestionsDomain():
    def __init__(self, repository) -> None:
        self._repository = repository

    def get_all_questions(self):
        return self._repository.get_all()

    def get_question(self, id: str):
        return self._repository.get_question(id)

    def create_question(self, question: CreateQuestionSchema):
        if not question.id:
            question.id = str(uuid4())
        return self._repository.create_question(question.dict())

    def update_question(self, question: UpdateQuestionSchema):
        return self._repository.update_question(question.dict(exclude_unset=True))

    def delete_question(self, id: str):
        return self._repository.delete_question(id)

questions_domain = QuestionsDomain(questions_repository)
