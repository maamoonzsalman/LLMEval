from sqlalchemy import select
from models.tables import TestPrompt
from core.database import SessionLocal

async def create_test_prompt(system_prompt_id, body):
    async with SessionLocal() as session:
        tp = TestPrompt(system_prompt_id=system_prompt_id, body=body)
        session.add(tp)
        await session.commit()
        await session.refresh(tp)
        return tp

