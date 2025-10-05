from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import List
from schemas.test_prompts import TestPromptOut

class SystemPromptCreate(BaseModel):
    title: str = Field(..., min_length = 1)
    body: str = Field(..., min_length = 1)

class SystemPromptOut(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class UpdateSystemPrompt(BaseModel):
    title: str | None = None
    body: str | None = None

class SystemWithTestPrompt(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
    test_prompts: List[TestPromptOut] = []
