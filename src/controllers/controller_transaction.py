from fastapi import APIRouter, Depends, status

from src.schemas.schema_transaction import TransactionCreateRequest, TransactionResponse


router = APIRouter(prefix="/transactions")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionResponse)
async def create_transaction(transaction: TransactionCreateRequest):
    pass