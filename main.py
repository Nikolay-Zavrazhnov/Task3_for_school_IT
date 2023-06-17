from fastapi import FastAPI

import app_user.models as models
from app_user.config import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
