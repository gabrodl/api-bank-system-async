from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.model_bank_accounts import BankAccounts
from src.schemas.schema_bank_accounts import BankAccountCreateRequest, BankAccountResponse

class BankAccountService:
    async def read_all(
        self,
        session: AsyncSession
        ) -> list[BankAccountResponse]:
        
        query = select(BankAccounts)
        
        result = await session.execute(query)
        
        bank_accounts = result.scalars().all()
        
        return [BankAccountResponse.model_validate(bank_account) for bank_account in bank_accounts]
    
    
    async def create(
        self,
        session: AsyncSession,
        bank_account: BankAccountCreateRequest
        ) -> BankAccountResponse:
        
        new_bank_account = BankAccounts(
            account_number=bank_account.account_number,
            balance=bank_account.balance,
        )
        
        session.add(new_bank_account)
        
        await session.commit()
        await session.refresh(new_bank_account)
        
        return BankAccountResponse.model_validate(new_bank_account)