from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from api.controllers.claude_controller import get_claude_output

router = APIRouter(
    prefix="/claude",
    tags=["claude"],
)

class GenerateRequest(BaseModel):
    system_prompt: str = Field(..., min_length = 1)
    test_prompt: str = Field(..., min_length = 1)
    max_output_tokens: int = Field(256, ge = 1, le = 4096)

class GenerateResponse(BaseModel):
    model: str
    text: str
    usage: dict | None = None

@router.post("/generate")
async def fetch_claude_output(req: GenerateRequest):
    try:
        data = get_claude_output(req.system_prompt, req.test_prompt, req.max_output_tokens)
        return data
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Gemini error: {e}")
