from core.database import SessionLocal
from models.tables import SystemPrompt
from sqlalchemy import select
from sqlalchemy.orm import selectinload

async def create_system_prompt(title, body):
    async with SessionLocal() as session:
        sp = SystemPrompt(title=title, body=body)
        session.add(sp)
        await session.commit()
        await session.refresh(sp)
        return sp

async def read_system_prompts():
   async with SessionLocal() as session:
        result = await session.execute(select(SystemPrompt))
        return result.scalars().all()
   
async def read_system_prompts_with_tests():
    async with SessionLocal() as session:
        result = await session.execute(select(SystemPrompt).options(selectinload(SystemPrompt.test_prompts)))
        return result.scalars().all()
   
async def update_system_prompt(id, title: str | None = None, body: str | None = None):
    async with SessionLocal() as session:
        sp = await session.get(SystemPrompt, id)

        if title is not None:
            sp.title = title
        if body is not None:
            sp.body = body

        await session.commit()
        await session.refresh(sp)
        return sp
    
async def delete_system_prompt(id: int):
    async with SessionLocal() as session:
        sp = await session.get(SystemPrompt, id)
        if sp is None:
            return False

        await session.delete(sp)
        await session.commit()
        return True
        

    
   

