from llm import get_llm

llm = get_llm()

def improver_agent(state):
    answer = state["input"]

    prompt = f"""
    Improve this interview answer:

    {answer}
    """

    response = llm.invoke(prompt).content.strip()

    return {**state, "improved_answer": response}