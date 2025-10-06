from fastapi import APIRouter
from api.controllers.test_prompt_controller import add_test_prompt, get_test_prompts, change_test_prompt, erase_test_prompt
from schemas.test_prompts import TestPromptOut, TestPromptCreate, UpdateTestPrompt
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/test_prompt",
    tags=["test_prompt"]
)


@router.post("/{system_prompt_id}", response_model=TestPromptOut)
async def insert_test_prompt(system_prompt_id: int, payload: TestPromptCreate):
    data = await add_test_prompt(system_prompt_id, payload.body)
    return data

@router.get("/{system_prompt_id}", response_model = list[TestPromptOut])
async def fetch_test_prompts(system_prompt_id: int):
    data = await get_test_prompts(system_prompt_id)
    return data

@router.put("/{id}", response_model=TestPromptOut)
async def modify_test_prompt(id: int, payload: UpdateTestPrompt):
    data = await change_test_prompt(id, payload.body)
    return data

@router.delete("/{id}")
async def destroy_system_prompt(id: int):
    data = await erase_test_prompt(id)
    return data