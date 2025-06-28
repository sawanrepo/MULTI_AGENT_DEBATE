from src.utils import call_llm
from src.agents.agent_a import get_agent_a_prompt
from langchain_core.messages import AIMessage
from src.loggers import log_message

def agent_a_node(state):
    prompt_template = get_agent_a_prompt()
    formatted_prompt = prompt_template.format(
        topic=state["topic"],
        round=state["round"],
        agent_a_args="\n- " + "\n- ".join(state["memory"]["agent_a"]),
        agent_b_args="\n- " + "\n- ".join(state["memory"]["agent_b"])
    )
    response = call_llm(formatted_prompt)
    message = AIMessage(content=response, name="Scientist")
    log_message(state, message)
    return {
        "messages": [message],
        "last_speaker": "Scientist"
    }