from core.llms.claude_llm import client, claude_model
from typing import Any, Dict
import time

def get_claude_output(system_prompt: str, test_prompt: str, max_output_tokens: int = 256) -> Dict[str, Any]:
    
    start = time.perf_counter()
    r = client.messages.create(
        model=claude_model,
        messages = [
            {"role": "assistant", "content": system_prompt},
            {"role": "user", "content": test_prompt},
        ],
        max_tokens = max_output_tokens
    )
    latency_ms = (time.perf_counter() - start) * 1000.0

    text = r.content[0].text

    usage = getattr(r, "usage", None)
    input_tokens = getattr(usage, "input_tokens", None) if usage else None
    output_tokens = getattr(usage, "output_tokens", None) if usage else None
    total_tokens = (input_tokens or 0) + (output_tokens or 0) if usage else None

    
    return {
        "model": claude_model,
        "text": text,
        "usage": {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens
        },
        "latency_ms": round(latency_ms, 2),
    }