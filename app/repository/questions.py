from app.repository.base import BaseRepository
from app.db import ddb_client
from app.config import config

class QuestionsRepository(BaseRepository):
    def __init__(self):
        super().__init__(
            db=ddb_client,
            table_name=config.QUESTIONS_TABLE,
            hash_key_name='id'
        )

    def get_question(self, id: str):
        return self.get(id)

    def create_question(self, question: dict):
        print(type(question), flush=True)
        print(question, flush=True)
        return self.create(question)

    def update_question(self, question: dict):
        id = question.get('id')
        question.pop('id')
        return self.update(id, question)

    def delete_question(self, id: str):
        return self.delete(id)

questions_repository = QuestionsRepository()
