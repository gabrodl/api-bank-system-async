from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.schema_transaction import TransactionCreateRequest, TransactionResponse
from src.services.service_transaction import TransactionService
from src.auth.depen import get_current_user
from src.database import get_session

router = APIRouter(prefix="/transactions", tags=["Transactions"])

service = TransactionService()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionResponse)
async def create_transaction(
    transaction: TransactionCreateRequest,
    session: AsyncSession = Depends(get_session),
    current_user: str = Depends(get_current_user)
    ):
    return await service.create(session, transaction)

@router.get("/{account_id}", status_code=status.HTTP_200_OK, response_model=list[TransactionResponse])
async def extract(
    account_id: int,
    session: AsyncSession = Depends(get_session),
    current_user: str = Depends(get_current_user)
):
    return await service.extract(session, account_id)