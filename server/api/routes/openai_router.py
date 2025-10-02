from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from api.controllers.openai_controller import get_openai_output

router = APIRouter(
    prefix="/openai",
    tags=["openai"]
)

class GenerateRequest(BaseModel):
    system_prompt: str = Field(..., min_length = 1)
    test_prompt: str = Field(..., min_length = 1)
    max_output_tokens: int = Field(256, ge=1, le=4096)

class GenerateResponse(BaseModel):
    model: str 
    text: str
    usage: dict | None = None

@router.post("/generate", response_model=GenerateResponse)
async def fetch_openai_output(req: GenerateRequest):
    try:
        data = get_openai_output(req.system_prompt, req.test_prompt, req.max_output_tokens)
        return data 
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"OpenAI error: {e}")