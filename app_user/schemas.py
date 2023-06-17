from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

from app_user.models import GenderType

T = TypeVar('T')


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    gender: GenderType = GenderType.unknown

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestUsers(BaseModel):
    parameter: UserSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
