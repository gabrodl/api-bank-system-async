from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from src.services.service_bank_accounts import BankAccountService
from src.schemas.schema_bank_accounts import (
    BankAccountCreateRequest,
    BankAccountResponse,
)


router = APIRouter(prefix="/bank-accounts", tags=["Bank Accounts"])

service = BankAccountService()

@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=BankAccountResponse)
async def create_bank_account(
    bank_account: BankAccountCreateRequest,
    session: AsyncSession = Depends(get_session)
    ):
    return await service.create(session, bank_account)