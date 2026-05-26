from sqlalchemy import ForeignKey, func
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, UTC

from src.database import Base


class BankAccounts(Base):
    __tablename__ = "bank_accounts"
    id:Mapped[int] = mapped_column(primary_key=True)
    account_number:Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    balance:Mapped[float] = mapped_column(default=0)
    created_at:Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at:Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True
    )