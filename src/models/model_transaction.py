from typing import List
import sqlalchemy as sa
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column 
from datetime import datetime
import enum

from src.database import Base


class TransactionType(enum.Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    
    
class Transactions(Base):
    __tablename__ = "transactions"
    id:Mapped[int] = mapped_column(primary_key=True)
    account_id:Mapped[int] = mapped_column(ForeignKey("bank_accounts.id"), nullable=False)
    type:Mapped[TransactionType] = mapped_column(sa.Enum(TransactionType, name="transactiontype"), nullable=False)
    amount:Mapped[float] = mapped_column(nullable=False)
    description:Mapped[str] = mapped_column(nullable=True)
    created_at:Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)