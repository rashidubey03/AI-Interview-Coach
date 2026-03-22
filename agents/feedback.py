from llm import get_llm

llm = get_llm()

def feedback_agent(state):
    answer = state["input"]

    prompt = f"""
    Give 3 short bullet points to improve this answer:

    {answer}
    """

    response = llm.invoke(prompt).content.strip()

    return {**state, "feedback": response}