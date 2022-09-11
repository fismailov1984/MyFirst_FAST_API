
from pydantic import BaseModel
from typing import Optional


class InfoSchemaIn(BaseModel):
    user_name: str
    wallet_number: str
    nickname: str
    balance: float


class InfoSchema(InfoSchemaIn):
    id: int


class UserSchemaIn(BaseModel):
    username: str
    password: str


class UserSchema(BaseModel):
    id: int
    username: str


class LoginSchema(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    username: Optional[str] = None


class InfoSchemaInPut(BaseModel):
    balance: float


class InfoSchemaPut(InfoSchemaInPut):
    user_name: str


class InfoSchemaInGetBalanse(BaseModel):
    balance: float

