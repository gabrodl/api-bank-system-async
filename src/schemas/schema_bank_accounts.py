from pydantic import BaseModel, ConfigDict
from datetime import datetime


class BankAccountCreateRequest(BaseModel):
    account_number: str
    balance: float
    
class BankAccountResponse(BaseModel):
    id: int
    account_number: str
    balance: float
    created_at: datetime
    updated_at: datetime | None
    
    model_config = ConfigDict(from_attributes=True)