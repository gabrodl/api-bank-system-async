from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from src.auth import security
from src.auth.schemas import (
    LoginRequest,
    LoginResponse,
)


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)   


FAKE_USER = {
    "email": "admin@admin.com",
    "password_hash": security.hash_password("admin123"),
}

@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest) -> LoginResponse:
    if data.email != FAKE_USER["email"] or not security.verify_password(
        data.password,
        FAKE_USER["password_hash"],
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
        
    password_valid = security.verify_password(
        data.password,
        FAKE_USER["password_hash"],
    )
    
    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
        )
        
    token = security.create_access_token(
        subject=data.email
    )
    
    return {
        "access_token": token,
        "token_type": "bearer",
    }