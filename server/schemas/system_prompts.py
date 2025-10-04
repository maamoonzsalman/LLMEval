from pydantic import BaseModel, ConfigDict
from datetime import datetime

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