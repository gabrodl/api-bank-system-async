from pydantic import BaseModel, PositiveFloat, ConfigDict
from datetime import datetime


class BankAccountCreateRequest(BaseModel):
    account_number: str
    balance: PositiveFloat
    created_at: datetime
    
class BankAccountResponse(BaseModel):
    account_number: str
    balance: float
    created_at: datetime
    updated_at: datetime | None
    
    model_config = ConfigDict(from_attributes=True)