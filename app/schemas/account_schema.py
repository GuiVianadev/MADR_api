from pydantic import BaseModel, EmailStr


class AccountSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class AccountPublic(BaseModel):
    id: int
    email: EmailStr
    username: str
