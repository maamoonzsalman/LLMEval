from utils.system_prompts_utils import create_system_prompt, read_system_prompts, update_system_prompt, delete_system_prompt

async def add_system_prompt(title: str, body: str):
    return await create_system_prompt(title, body)

async def get_system_prompts():
    return await read_system_prompts()

async def change_system_prompt(id: int, title: str | None = None, body: str | None = None):
    return await update_system_prompt(id, title, body)

async def erase_system_prompt(id: int):
    return await delete_system_prompt(id)




