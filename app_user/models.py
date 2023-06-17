from sqlalchemy import Column, Integer, String
from app_user.config import Base

from enum import Enum


class GenderType(str, Enum):
    man = "man"
    woman = "woman"
    unknown = "unknown"

class User(Base):
    __tablename__ = "table_user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)