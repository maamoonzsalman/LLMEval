from utils.metrics_utils import eval_answer_relevancy, eval_answer_completeness, eval_reasoning_quality, eval_instruction_adherence, eval_clarity_structure

def get_metrics(system_prompt: str, test_prompt: str, candidate_output):
    
    relevancy = eval_answer_relevancy(test_prompt, candidate_output)
    completeness = eval_answer_completeness(system_prompt, test_prompt, candidate_output)
    reasoning = eval_reasoning_quality(test_prompt, candidate_output)
    adherence = eval_instruction_adherence(system_prompt, test_prompt, candidate_output)
    clarity = eval_clarity_structure(test_prompt, candidate_output)
    
    return {
        "relevancy": relevancy, 
        "completeness": completeness,
        "reasoning": reasoning,
        "adherence": adherence,
        "clarity": clarity
    }