from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app_user.config import SessionLocal
from app_user.crud import create_user, get_user, get_user_by_gender, get_user_by_id
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


# Получить все записи из БД с возможностью лимита
@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_user(db, skip, limit)

    return Response(status="Ok", code="200", message="Success fetch all data", result=users)


# получить список строк из таблицы БД по значению из столбца gender возможностью лимита
@router.get("/{gender}")
async def get_users_gender(gender: str=None, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    users = get_user_by_gender(db, gender, skip, limit)

    return Response(status="Ok", code="200", message="Success fetch all data", result=users)

# Получить запись по конкретному id
@router.get("/{id}")
async def get_users_id(id: int, db: Session = Depends(get_db)):
    users = get_user_by_id(db, id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=users).dict(exclude_none=True)
