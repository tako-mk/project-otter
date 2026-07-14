from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database import Base

class Group(Base):
    __tablename__ = "groups"

    # id 主キー 
    id: Mapped[int] = mapped_column(primary_key=True)

    # name グループネーム
    name: Mapped[str] = mapped_column(String(100))

    # parent_id 親グループID
    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey("groups.id"),
        nullable=True
    )