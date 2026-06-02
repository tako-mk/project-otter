from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./data/app.db" # dbの位置

engine = create_engine(     # DB接続のための設定
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(    # DB操作メソッド
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()   # テーブルの親クラス