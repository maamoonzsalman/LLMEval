from pydantic import BaseModel

class ExperimentRequest(BaseModel):
    system_prompt: str
    test_prompt: str