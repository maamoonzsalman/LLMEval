from typing import AsyncGenerator
from core.database import SessionLocal

async def get_db() -> AsyncGenerator:
    async with SessionLocal() as session:
        # no need to commit/rollback here; do it in your repo/handler
        yield session
