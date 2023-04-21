from enum import Enum

from pydantic import BaseModel


class UserRoleEnum(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    username: str = None
    password: str = None
    role: str = UserRoleEnum.user


class UserInDB(User):
    hashed_password: str


class UserLogin(BaseModel):
    username: str = None
    password: str = None
