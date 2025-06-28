def update_memory_node(state):
    message = state["messages"][-1]
    speaker = message.name  

    if speaker == "Scientist":
        state["memory"]["agent_a"].append(message.content.strip())
    elif speaker == "Philosopher":
        state["memory"]["agent_b"].append(message.content.strip())
    return state