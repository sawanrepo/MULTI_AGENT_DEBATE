from langchain.prompts import ChatPromptTemplate

def get_agent_a_prompt():
    return ChatPromptTemplate.from_template("""You are a Scientist participating in a formal debate.

Debate Topic: "{topic}"
Current Round: {round}

Your previous arguments:
{agent_a_args}

Philosopher's previous arguments:
{agent_b_args}

Instructions:
- Give a new logical, evidence-based scientific argument.
- Do not repeat yourself.
- Respond to the philosopher’s points if applicable.
- If this is Round 1, start the debate strongly by presenting your opening stance on the topic.""")