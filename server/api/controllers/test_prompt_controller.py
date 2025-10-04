from utils.test_prompts_utils import create_test_prompt, read_test_prompts

async def add_test_prompt(system_prompt_id: int, body: str):
    return await create_test_prompt(system_prompt_id, body)

async def get_test_prompts(system_prompt_id: int):
    return await read_test_prompts(system_prompt_id)