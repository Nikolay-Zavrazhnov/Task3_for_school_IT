from sqlalchemy.orm import Session

from app_user.models import User
from app_user.schemas import UserSchema


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_gender(db: Session, gender=None, skip: int = 0, limit: int = 100):
    result = db.query(User).all()
    list = []
    for user in result:
        if user.gender == gender:
            list.append(user)

    return list[skip:][:limit]


def create_user(db: Session, user: UserSchema):
    new_user = User(name=user.name, gender=user.gender)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def remove_user(db: Session, user_id: int):
    some_user = get_user_by_id(db=db, user_id=user_id)
    db.delete(some_user)
    db.commit()


def update_user(db: Session, user_id: int, name: str, gender: str):
    some_user = get_user_by_id(db=db, user_id=user_id)

    some_user.name = name
    some_user.gender = gender

    db.commit()
    db.refresh(some_user)
    return some_user
