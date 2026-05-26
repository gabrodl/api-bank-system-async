from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth import security
from src.database import AsyncSessionLocal


bearer_scheme = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    token =  credentials.credentials
    
    payload = security.decode_access_token(token)
    
    subject = payload.get("sub")
    
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
        
    return subject


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session