from llm import get_llm

llm = get_llm()

def evaluator_agent(state):
    answer = state["input"]

    prompt = f"""
    Evaluate this interview answer.

    Answer: {answer}

    Give score out of 10 and 1 line reason.
    """

    response = llm.invoke(prompt).content.strip()

    return {**state, "evaluation": response}