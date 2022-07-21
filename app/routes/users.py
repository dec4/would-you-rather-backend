from fastapi import APIRouter
from fastapi import HTTPException

from app.domain.users import users_domain
from app.schemas.users import CreateUserSchema
from app.schemas.users import UpdateUserSchema

class UsersRouter:
    def __init__(self, domain) -> None:
        self._domain = domain

    @property
    def router(self):
        api_router = APIRouter(prefix='/users', tags=['users'])

        @api_router.get('/')
        def index_route():
            return 'Hello! Welcome to users index route'

        @api_router.get('/all')
        def get_all():
            return self._domain.get_all_users()

        @api_router.post('/create')
        def create_user(user_model: CreateUserSchema):
            return self._domain.create_user(user_model)

        @api_router.get('/get/{user_id}')
        def get_user(user_id: str):
            try:
                return self._domain.get_user(user_id)
            except KeyError:
                raise HTTPException(status_code=400, detail='No user found')

        @api_router.put('/update')
        def update_user(user_model: UpdateUserSchema):
            return self._domain.update_user(user_model)

        @api_router.delete('/delete/{user_id}')
        def delete_user(user_id: str):
            return self._domain.delete_user(user_id)

        return api_router

users_router = UsersRouter(users_domain).router
