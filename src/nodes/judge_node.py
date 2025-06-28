from src.utils import call_llm
from langchain.prompts import ChatPromptTemplate
from src.loggers import log_message
from langchain_core.messages import AIMessage
def judge_node(state):
    prompt = ChatPromptTemplate.from_template("""You are a neutral judge evaluating a debate.

Debate Topic: "{topic}"

Scientist's arguments:
{agent_a_args}

Philosopher's arguments:
{agent_b_args}

Summarize the debate clearly.
Then, declare the winner based on logic, clarity, and relevance.
Output must follow this format:

Summary:
<summary>

Winner:
<Scientist or Philosopher>

Justification:
<reason why they won>
""")

    formatted_prompt = prompt.format(
        topic=state["topic"],
        agent_a_args="\n- " + "\n- ".join(state["memory"]["agent_a"]),
        agent_b_args="\n- " + "\n- ".join(state["memory"]["agent_b"])
    )

    response = call_llm(formatted_prompt)
    msg = AIMessage(content=response, name="Judge")
    log_message(state, msg, is_judge=True)
    return {"messages": [msg], "last_speaker": "Judge", "__end__": True}