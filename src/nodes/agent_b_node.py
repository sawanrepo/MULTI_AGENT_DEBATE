from src.utils import call_llm
from src.agents.agent_b import get_agent_b_prompt
from langchain_core.messages import AIMessage
from src.loggers import log_message

def agent_b_node(state):
    prompt_template = get_agent_b_prompt()
    formatted_prompt = prompt_template.format(
        topic=state["topic"],
        round=state["round"],
        agent_b_args="\n- " + "\n- ".join(state["memory"]["agent_b"]),
        agent_a_args="\n- " + "\n- ".join(state["memory"]["agent_a"])
    )
    response = call_llm(formatted_prompt)
    msg = AIMessage(content=response, name="Philosopher")
    log_message(state, msg)
    return {"messages": [msg], "last_speaker": "Philosopher"}