from core.llms.openai_llm import client, openai_model

def get_openai_output(system_prompt: str, test_prompt: str, max_output_tokens: int = 256):
    r = client.responses.create(
        model = openai_model,
        input = [
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": test_prompt},
        ],
        max_output_tokens=max_output_tokens
    )

    text = getattr(r, "output_text", None)
    if not text:
        parts = []
        for item in getattr(r, "output", []) or []:
            for p in (getattr(item, "content", None) or []):
                t = getattr(p, "text", None) or (p.get("text") if isinstance(p, dict) else None)
                if t:
                    parts.append(t)
        text = "".join(parts) if parts else ""

    # document reason if incomplete
    if getattr(r, "status", None) == "incomplete" and not text:
        reason = getattr(getattr(r, "incomplete_details", None), "reason", None)
        text = f"[incomplete: {reason or 'unknown'}]"
    
    usage = getattr(r, "usage", None)

    return {
        "model": openai_model,
        "text": (text or "").strip(),
        "usage": {
            "input_tokens": getattr(usage, "input_tokens", None) if usage else None,
            "output_tokens": getattr(usage, "output_tokens", None) if usage else None,
            "total_tokens": getattr(usage, "total_tokens", None) if usage else None
        }
    }