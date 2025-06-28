from langchain.prompts import ChatPromptTemplate

def get_agent_b_prompt():
    return ChatPromptTemplate.from_template("""You are a Philosopher in a debate.

Debate Topic: "{topic}"
Round: {round}

Your previous arguments:
{agent_b_args}

Scientist's arguments:
{agent_a_args}
Instructions:
Give a new thoughtful and ethical argument.
Do not repeat yourself. Respond to the scientist’s reasoning where appropriate.""")