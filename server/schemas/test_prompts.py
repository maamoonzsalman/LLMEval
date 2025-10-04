from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class TestPromptCreate(BaseModel):
    body: str = Field(..., min_length = 1)

class TestPromptOut(BaseModel):
    id: int
    body: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)