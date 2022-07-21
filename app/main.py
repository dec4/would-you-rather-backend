import uvicorn
from fastapi import FastAPI

from app.routes.users import users_router


app = FastAPI(title="Would You Rather Backend")
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"hello": "world"}

if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
