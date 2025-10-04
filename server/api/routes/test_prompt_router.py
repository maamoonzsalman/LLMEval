from fastapi import APIRouter
from api.controllers.test_prompt_controller import create_test_prompt
from schemas.test_prompts import TestPromptOut, TestPromptCreate
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/test_prompt",
    tags=["test_prompt"]
)


@router.post("/{system_prompt_id}", response_model=TestPromptOut)
async def insert_test_prompt(system_prompt_id: int, payload: TestPromptCreate):
    data = await create_test_prompt(system_prompt_id, payload.body)
    return data
