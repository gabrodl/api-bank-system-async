from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import engine
from src.controllers.controller_bank_acounts import router as router_bank_accounts
from src.controllers.controller_transaction import router as router_transaction
from src.auth.controller import router as router_auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    await engine.dispose()


app = FastAPI(
    title="bank_system_async",
    lifespan=lifespan,
)

app.include_router(router_auth)
app.include_router(router_bank_accounts)
app.include_router(router_transaction)