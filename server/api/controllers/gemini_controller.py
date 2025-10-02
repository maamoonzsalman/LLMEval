from core.llms.gemini_llm import gemini_model, GEMINI_MODEL_ID
from typing import Any, Dict
import google.generativeai as genai

def get_gemini_output(system_prompt: str, test_prompt: str, max_output_tokens: int = 256) -> Dict[str, Any]:
    
    model = (
        genai.GenerativeModel(model_name=GEMINI_MODEL_ID, system_instruction=system_prompt)
        if system_prompt else gemini_model
    )
    
    r = model.generate_content(
        test_prompt,
        generation_config={"max_output_tokens": max_output_tokens},
    )

    text = getattr(r, "text", "") or ""

    usage = getattr(r, "usage_metadata", None)
    usage_out = None

    if usage:
        usage_out = {
            "input_tokens": getattr(usage, "prompt_token_count", None),
            "output_tokens": getattr(usage, "candidates_token_count", None),
            "total_tokens": getattr(usage, "total_token_count", None),
        }

    return {
        "model": "gemini-2.5-pro",
        "text": text.strip(),
        "usage": usage_out, 
    }