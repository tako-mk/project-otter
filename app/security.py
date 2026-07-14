from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User

# JWT認証用アクセストークン関係の定義
SECRET_KEY = "おはこんばんちは"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ヘッダからアクセストークンを取り出す
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)

# パスワード
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# パスワードハッシュ化関数
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# パスワード認証関数
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# アクセストークンの作成
def create_access_token(user_id: int) -> str:

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

# アクセストークンのデコード 対応したuser_idを返す
def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            return None

        return int(user_id)

    except JWTError:
        return None
