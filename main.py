from fastapi import FastAPI

import app_user.models as models
from app_user.config import engine
from app_user.routers import router

app = FastAPI()


@app.get("/")
def get_hello():
    return f"hi! I'm FASTAPI, go to http://127.0.0.1:8000/docs"


models.Base.metadata.create_all(bind=engine)
app.include_router(router, prefix="/Action_with_users", tags=["users"])