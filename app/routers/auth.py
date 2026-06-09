from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.security import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()

    return {"message": "user created"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email)

    if db_user is None:
        raise HTTPException(status_code=400, detail="そのメールアドレスは登録されていません")

    if verify_password(user.password, db_user.password_hash):
        return {"message": "login success"}
    else:
        raise HTTPException(status_code=401, detail="メールアドレスまたはパスワードが違います")