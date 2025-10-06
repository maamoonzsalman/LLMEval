from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams


def eval_answer_relevancy(test_prompt: str, candidate_output: str):
    test_case = LLMTestCase(input=test_prompt, actual_output=candidate_output)

    rubric = (
        "You are an evaluation judge. Score ANSWER RELEVANCE only: how directly and substantively the answer "
        "addresses the USER's request. Penalize off-topic content, deflection, boilerplate, or restating the "
        "question without answering. Ignore style/format/tone and do not fact-check beyond basic plausibility. "
        "Be concise.\n\n"
        "Anchors:\n"
        "5 = Direct, focused, and fully pertinent to the request\n"
        "4 = Mostly relevant; minor tangents or missing small parts\n"
        "3 = Partly relevant; mixes on-topic and off-topic or shallowly addresses the request\n"
        "2 = Largely irrelevant; significant drift or avoidance\n"
        "1 = Not relevant to the request\n"
        "Reply briefly."
    )

    metric = GEval(
        name="Answer Relevance",
        criteria=rubric,
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.7,
        model="gpt-4o",
    )

    metric.measure(test_case)

    score01 = float(metric.score or 0.0)
    score15 = int(round(1 + 4 * score01))

    return {
        "metric": "answer_relevance",
        "score_0_to_1": score01,
        "score_1_to_5": score15,
        "passed": bool(score01 >= metric.threshold),
        "reason": getattr(metric, "reason", None),
    }

def eval_answer_completeness(system_prompt: str, test_prompt: str, candidate_output: str):
    test_case = LLMTestCase(input=test_prompt, actual_output=candidate_output)

    rubric = (
            "You are an evaluation judge. Score how completely the Assistant’s answer covers what the USER asked for, "
            "considering the SYSTEM instructions. Judge coverage only (not style or factuality).\n\n"
            "System Instructions:\n"
            f"{system_prompt}\n\n"
            "Anchors:\n"
            "5 = Fully complete (all requested elements covered; no major omissions)\n"
            "4 = Mostly complete (minor omissions)\n"
            "3 = Partially complete (several required parts missing or shallow)\n"
            "2 = Mostly incomplete (touches topic, misses most elements)\n"
            "1 = Not complete (fails to answer or off-topic)\n\n"
            "Reply briefly."
    )
    
    metric = GEval(
        name="Completeness",
        criteria=rubric,
        evaluation_params=[LLMTestCaseParams.INPUT ,LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.7,
        model="gpt-4o"
    )

    metric.measure(test_case)

    # Map the 0-1 score to 1-5
    score01 = float(metric.score or 0.0)
    score15 = int(round(1 + 4 * score01))

    return {
        "metric": "completeness",
        "score_0_to_1": score01,
        "score_1_to_5": score15,
        "passed": bool(score01 >= metric.threshold),
        "reason": getattr(metric, "reason", None), 
    }

def eval_reasoning_quality(test_prompt: str, candidate_output: str):
    test_case = LLMTestCase(input=test_prompt, actual_output=candidate_output)

    rubric = (
        "You are an evaluation judge. Score the REASONING QUALITY of the Assistant’s answer only. "
        "Look for: sound stepwise logic, correct causal links, acknowledgement of assumptions/trade-offs, "
        "and absence of contradictions or non-sequiturs. Judge the reasoning visible in the answer; "
        "do not fact-check beyond plausibility.\n\n"
        "Anchors:\n"
        "5 = Rigorous, coherent reasoning with explicit assumptions/trade-offs; no contradictions\n"
        "4 = Solid reasoning with minor gaps or unstated assumptions\n"
        "3 = Mixed: some valid reasoning but noticeable leaps or thin justification\n"
        "2 = Weak: hand-wavy, multiple leaps, or partial contradictions\n"
        "1 = Flawed: illogical, self-contradictory, or off-topic reasoning\n"
        "Reply briefly."
    )

    metric = GEval(
        name="Reasoning Quality",
        criteria=rubric,
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.7,
        model="gpt-4o",
    )

    metric.measure(test_case)
    score01 = float(metric.score or 0.0)
    score15 = int(round(1 + 4 * score01))

    return {
        "metric": "reasoning_quality",
        "score_0_to_1": score01,
        "score_1_to_5": score15,
        "passed": bool(score01 >= metric.threshold),
        "reason": getattr(metric, "reason", None),
    }


def eval_instruction_adherence(system_prompt: str, test_prompt: str, candidate_output: str):
    test_case = LLMTestCase(input=test_prompt, actual_output=candidate_output)

    rubric = (
        "You are an evaluation judge. Score INSTRUCTION/PERSONA ADHERENCE: "
        "how well the Assistant follows the SYSTEM role/tone/constraints and any explicit formatting rules.\n\n"
        "System Instructions:\n"
        f"{system_prompt}\n\n"
        "Judge: role consistency, tone, constraints (e.g., word limits, sections, JSON schema), and avoidance of "
        "unasked content or disclaimers. Consider the USER input only for constraints implied by it.\n\n"
        "Anchors:\n"
        "5 = Perfect adherence to role, tone, and all explicit constraints\n"
        "4 = Minor lapses (e.g., tiny format/wording drift) but overall compliant\n"
        "3 = Mixed adherence; notable misses on tone/format/constraints\n"
        "2 = Poor adherence; many constraints ignored\n"
        "1 = Not aligned with instructions or persona\n"
        "Reply briefly."
    )

    metric = GEval(
        name="Instruction/Persona Adherence",
        criteria=rubric,
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.7,
        model="gpt-4o",
    )

    metric.measure(test_case)
    score01 = float(metric.score or 0.0)
    score15 = int(round(1 + 4 * score01))

    return {
        "metric": "instruction_adherence",
        "score_0_to_1": score01,
        "score_1_to_5": score15,
        "passed": bool(score01 >= metric.threshold),
        "reason": getattr(metric, "reason", None),
    }


def eval_clarity_structure(test_prompt: str, candidate_output: str):
    test_case = LLMTestCase(input=test_prompt, actual_output=candidate_output)

    rubric = (
        "You are an evaluation judge. Score CLARITY & STRUCTURE of the Assistant’s answer. "
        "Assess organization, scannability, and concise expression. Prefer clear headings/lists when helpful, "
        "consistent formatting, and minimal redundancy. Do not judge factual correctness.\n\n"
        "Anchors:\n"
        "5 = Exceptionally clear, well-structured, concise; easy to scan\n"
        "4 = Clear and organized with minor verbosity or small structure issues\n"
        "3 = Understandable but somewhat rambling or poorly organized\n"
        "2 = Hard to follow; weak structure and verbosity\n"
        "1 = Unclear, disorganized, or confusing\n"
        "Reply briefly."
    )

    metric = GEval(
        name="Clarity & Structure",
        criteria=rubric,
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.7,
        model="gpt-4o",
    )

    metric.measure(test_case)
    score01 = float(metric.score or 0.0)
    score15 = int(round(1 + 4 * score01))

    return {
        "metric": "clarity_structure",
        "score_0_to_1": score01,
        "score_1_to_5": score15,
        "passed": bool(score01 >= metric.threshold),
        "reason": getattr(metric, "reason", None),
    }