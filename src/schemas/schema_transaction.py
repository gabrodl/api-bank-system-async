from pydantic import BaseModel, Field, ConfigDict
from src.models.model_transaction import TransactionType
from datetime import datetime

    
class TransactionCreateRequest(BaseModel):
    account_id: int
    amount: float
    type: TransactionType
    description: str | None = None
    
class TransactionResponse(BaseModel):
    description: str | None = None
    id: int
    account_id: int
    type: TransactionType
    amount: float
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)