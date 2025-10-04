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
    
async def read_test_prompts(system_prompt_id):
    async with SessionLocal() as session:
        result = await session.execute(
            select(TestPrompt)
            .where(TestPrompt.system_prompt_id == system_prompt_id)
            .order_by(TestPrompt.created_at.desc())
        )
        return result.scalars().all()
    
async def update_test_prompt(id: int, body: str | None = None):
    async with SessionLocal() as session:
        tp = await session.get(TestPrompt, id)

        if body is not None:
            tp.body = body

        await session.commit()
        await session.refresh(tp)

        return tp
    
