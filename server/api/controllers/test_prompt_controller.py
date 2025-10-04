from utils.test_prompts_utils import create_test_prompt

async def add_test_prompt(system_prompt_id: int, body: str):
    return await create_test_prompt(system_prompt_id, body)
