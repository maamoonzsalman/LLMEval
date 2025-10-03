from fastapi import APIRouter, HTTPException
from api.controllers.system_prompt_controller import get_system_prompts, add_system_prompt, change_system_prompt, erase_system_prompt
from schemas.system_prompts import SystemPromptOut
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/system_prompt",
    tags=["system_prompt"]
)

class GenerateRequest(BaseModel):
    title: str = Field(..., min_length = 1)
    body: str = Field(..., min_length = 1)

@router.post("/", response_model=SystemPromptOut)
async def insert_system_prompt(req: GenerateRequest):
    data = await add_system_prompt(req.title, req.body)
    return data

@router.get("/", response_model=list[SystemPromptOut])
async def fetch_system_prompts():
    data = await get_system_prompts()
    return data

@router.put("/", response_model=SystemPromptOut)
async def modify_system_prompts(id: int, title: str | None = None, body: str | None = None):
    data = await change_system_prompt(id, title, body)
    return data 

@router.delete("/")
async def destroy_system_prompt(id: int):
    data = await erase_system_prompt(id)
    return data


