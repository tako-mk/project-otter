from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./data/app.db" # dbの位置

engine = create_engine(     # DB接続のための設定
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(    # DB接続初期化メソッド
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()   # テーブルの親クラス

# 実際にDB接続を確立する
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()