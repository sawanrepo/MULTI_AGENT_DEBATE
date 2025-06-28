from langgraph.graph import StateGraph, add_messages, END
from typing import TypedDict, Annotated
from src.nodes.agent_a_node import agent_a_node
from src.nodes.agent_b_node import agent_b_node
from src.nodes.memory_node import update_memory_node
from src.nodes.judge_node import judge_node

class DebateState(TypedDict):
    topic: str
    round: int
    memory: dict
    messages: Annotated[list, add_messages]

def increment_round_node(state):
    return {"round": state["round"] + 1}

def next_agent(state: DebateState) -> str:
    if state["round"] >= 9: 
        return "judge"
    if state["round"] % 2 == 1:
        return "agent_a"
    else:
        return "agent_b"

graph = StateGraph(DebateState)

graph.add_node("agent_a", agent_a_node)
graph.add_node("agent_b", agent_b_node)
graph.add_node("memory", update_memory_node)
graph.add_node("increment", increment_round_node)
graph.add_node("judge", judge_node)

graph.set_entry_point("agent_a")

graph.add_edge("agent_a", "memory")
graph.add_edge("agent_b", "memory")
graph.add_edge("memory", "increment")

graph.add_conditional_edges(
    "increment",
    next_agent,
    {
        "agent_a": "agent_a",
        "agent_b": "agent_b",
        "judge": "judge",
    }
)

graph.add_edge("judge", END)
debate_dag = graph.compile()