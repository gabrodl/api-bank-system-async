from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from http.client import HTTPException

from src.models.model_transaction import TransactionType, Transactions
from src.schemas.schema_transaction import TransactionCreateRequest, TransactionResponse
from src.models.model_bank_accounts import BankAccounts

class TransactionService:
    async def create(self, session: AsyncSession, transaction: TransactionCreateRequest) -> TransactionResponse:
        new_transaction = Transactions(
            account_id=transaction.account_id,
            amount=transaction.amount,
            type=transaction.type
        )
        
        result = await session.execute(
            select(BankAccounts).where(
                BankAccounts.id == transaction.account_id
            )
        )

        bank_account = result.scalar_one_or_none()
        
        if not bank_account:
            raise HTTPException(status_code=404, detail="Bank account not found")
        
        if transaction.type == TransactionType.DEPOSIT:
            bank_account.balance += transaction.amount
        elif transaction.type == TransactionType.WITHDRAW:
            if bank_account.balance < transaction.amount:
                raise HTTPException(status_code=400, detail="Insufficient funds")
            bank_account.balance -= transaction.amount
        

        session.add(new_transaction)
        
        await session.commit()
        await session.refresh(new_transaction)
        
        return TransactionResponse.model_validate(new_transaction)
    
    async def extract(
        self,
        session: AsyncSession,
        account_id: int
        ) -> list[TransactionResponse]:
        
        query = select(Transactions).where(Transactions.account_id == account_id)
        
        result = await session.execute(query)
        
        transactions = result.scalars().all()
        
        return [TransactionResponse.model_validate(transaction) for transaction in transactions]
    