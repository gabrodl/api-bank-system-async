from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import engine
from src.controllers import controller_bank_acounts, controller_transaction


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    await engine.dispose()


app = FastAPI(
    title="bank_system_async",
    lifespan=lifespan,
)

app.include_router(controller_bank_acounts.router)
app.include_router(controller_transaction.router)