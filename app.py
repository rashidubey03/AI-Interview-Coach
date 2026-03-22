from langgraph.graph import StateGraph, END
from typing import TypedDict

from agents.evaluator import evaluator_agent
from agents.feedback import feedback_agent
from agents.improver import improver_agent


# ✅ FIXED STATE
class State(TypedDict, total=False):
    input: str
    evaluation: str
    feedback: str
    improved_answer: str


# ✅ SIMPLE BRANCHING
def route(state):
    evaluation = state["evaluation"]

    if "9" in evaluation or "10" in evaluation:
        return END
    return "feedback"


# build graph
builder = StateGraph(State)

builder.add_node("evaluate", evaluator_agent)
builder.add_node("feedback", feedback_agent)
builder.add_node("improve", improver_agent)

builder.set_entry_point("evaluate")

builder.add_conditional_edges("evaluate", route)

builder.add_edge("feedback", "improve")
builder.add_edge("improve", END)

graph = builder.compile()


# run
if __name__ == "__main__":
    user_input = input("Enter your answer: ")

    result = graph.invoke({
        "input": user_input
    })

    print("\n--- RESULT ---\n")
    print(result)