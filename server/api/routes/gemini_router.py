from fastapi import APIRouter, HTTPException
from core.llms.gemini_llm import gemini_model
from pydantic import BaseModel, Field
from api.controllers.gemini_controller import get_gemini_output

router = APIRouter(
    prefix="/gemini",
    tags=["gemini"]
)

class GenerateRequest(BaseModel):
    system_prompt: str = Field(..., min_length = 1)
    test_prompt: str = Field(..., min_length = 1)
    max_output_tokens: int = Field(1024, ge = 1, le = 4096)

class GenerateResponse(BaseModel):
    model: str 
    text: str
    usage: dict | None = None


@router.post("/generate", response_model = GenerateResponse)
async def fetch_gemini_output(req: GenerateRequest):
    try:
        data = get_gemini_output(req.system_prompt, req.test_prompt, req.max_output_tokens)
        return data
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Gemini error: {e}")