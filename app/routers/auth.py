from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=user.password
    )

    db.add(db_user)
    db.commit()

    return {"message": "user created"}