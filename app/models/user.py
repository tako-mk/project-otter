from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    # id 主キー 
    id: Mapped[int] = mapped_column(primary_key=True)

    # username ユーザーネーム
    username: Mapped[str] = mapped_column(String(50))

    # email メールアドレス
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )

    # password_hash パスワード(ハッシュ)
    password_hash: Mapped[str] = mapped_column(
        String(255),
    )