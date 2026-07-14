from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.security import verify_token, oauth2_scheme

# user取得
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = verify_token(token)

    if user_id is None:
        raise HTTPException(status_code=401, detail="認証に失敗しました")

    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=401, detail="ユーザーが存在しません")

    return db_user