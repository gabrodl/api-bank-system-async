from pydantic import BaseModel, Field
from src.models.model_transaction import TransactionType
from datetime import datetime

    
class TransactionCreateRequest(BaseModel):
    description: str = Field(max_length=40)
    type: TransactionType
    account_id: int
    amount: float
    
class TransactionResponse(BaseModel):
    description: str
    account_id: int
    type: TransactionType
    amount: float
    created_at: datetime