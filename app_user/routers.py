from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app_user.config import SessionLocal
from app_user.crud import create_user
from app_user.schemas import RequestUsers, Response

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_user_service(request: RequestUsers, db: Session = Depends(get_db)):
    create_user(db, user=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Entry created successfully").dict(exclude_none=True)