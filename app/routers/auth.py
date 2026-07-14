from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.security import hash_password, verify_password, create_access_token, verify_token
from app.services.auth_services import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
        user_type=user.user_type
    )

    db.add(db_user)
    db.commit()

    return {"message": "user created"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user is None:
        raise HTTPException(status_code=400, detail="そのメールアドレスは登録されていません")

    if verify_password(user.password, db_user.password_hash):
        token = create_access_token(
            db_user.id
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }
    else:
        raise HTTPException(status_code=401, detail="メールアドレスまたはパスワードが違います")

@router.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }

@router.get("/test-token")
def test_token(token: str):
    return verify_token(token)