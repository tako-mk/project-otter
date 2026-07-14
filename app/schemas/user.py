from pydantic import BaseModel, EmailStr

# ユーザー側が受け取る
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    user_type: str

class UserLogin(BaseModel):
    email: str
    password: str