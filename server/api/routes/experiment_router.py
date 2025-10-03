import asyncio
from fastapi import APIRouter, HTTPException
from api.controllers.gemini_controller import get_gemini_output
from api.controllers.openai_controller import get_openai_output
from api.controllers.claude_controller import get_claude_output
from api.controllers.experiment_controller import get_metrics

router = APIRouter(
    prefix="/experiment",
    tags=["experiment"]
)

@router.post("/run")
async def get_eval_metrics(system_prompt: str, test_prompt: str):
    try:

        gem_task = asyncio.to_thread(get_gemini_output, system_prompt, test_prompt, max_output_tokens=1024)
        oai_task = asyncio.to_thread(get_openai_output, system_prompt, test_prompt, max_output_tokens=1024)
        cla_task = asyncio.to_thread(get_claude_output, system_prompt, test_prompt, max_output_tokens=1024)

        gemini_output, openai_output, claude_output = await asyncio.gather(
            gem_task, oai_task, cla_task
        )

        g_metrics_task = asyncio.to_thread(get_metrics, system_prompt, test_prompt, gemini_output["text"])
        o_metrics_task = asyncio.to_thread(get_metrics, system_prompt, test_prompt, openai_output["text"])
        c_metrics_task = asyncio.to_thread(get_metrics, system_prompt, test_prompt, claude_output["text"])

        gemini_metrics, openai_metrics, claude_metrics = await asyncio.gather(
            g_metrics_task, o_metrics_task, c_metrics_task
        )
        
        return {
            "scores": {
                "gemini_score": gemini_metrics,
                "openai_score": openai_metrics,
                "claude_score": claude_metrics,
            },
            "output": {
                "gemini_output": gemini_output,
                "openai_output": openai_output,
                "claude_output": claude_output,
            }
        }      
    
    except Exception as e:
         raise HTTPException(status_code=502, detail=f"Error evaluating LLMs: {e}")
