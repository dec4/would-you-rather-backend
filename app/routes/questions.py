from fastapi import APIRouter
from fastapi import HTTPException

from app.domain.questions import questions_domain
from app.schemas.questions import CreateQuestionSchema
from app.schemas.questions import UpdateQuestionSchema

class QuestionsRouter:
    def __init__(self, domain) -> None:
        self._domain = domain

    @property
    def router(self):
        api_router = APIRouter(prefix='/questions', tags=['questions'])

        @api_router.get('/')
        def index_route():
            return 'Hello! Welcome to questions index route'

        @api_router.get('/all')
        def get_all():
            return self._domain.get_all_questions()

        @api_router.post('/create')
        def create_question(question_model: CreateQuestionSchema):
            return self._domain.create_question(question_model)

        @api_router.get('/get/{qid}')
        def get_question(qid: str):
            try:
                return self._domain.get_question(qid)
            except KeyError:
                raise HTTPException(status_code=404, detail='No question found')

        @api_router.put('/update')
        def update_question(question_model: UpdateQuestionSchema):
            return self._domain.update_question(question_model)

        @api_router.delete('/delete/{qid}')
        def delete_question(qid: str):
            return self._domain.delete_question(qid)

        return api_router

questions_router = QuestionsRouter(questions_domain).router
