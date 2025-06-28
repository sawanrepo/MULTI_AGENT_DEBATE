from src.dag.debate_dag import debate_dag
from src.user_input import get_debate_topic
from langchain_core.messages import AIMessage
def main():
    topic = get_debate_topic()
    initial_state = {
        "topic": topic,
        "round": 1,
        "memory": {"agent_a": [], "agent_b": []},
        "messages": []
    }

    print(f"\n🔮 Starting Debate on: \"{topic}\"\n")
    print("="*50 + "\n")
    printed_message_ids = set()
    current_state = initial_state.copy()
    
    for step in debate_dag.stream(initial_state,config={"recursion_limit": 35}):
        for key, value in step.items():
            if isinstance(value, dict):
                current_state.update(value)
        messages = current_state.get("messages", [])
        current_round = current_state.get("round", 1)
        for message in messages:
            if (isinstance(message, AIMessage) and 
                id(message) not in printed_message_ids and
                message.name in ["Scientist", "Philosopher", "Judge"]):
                printed_message_ids.add(id(message))
                speaker_emoji = "🔬" if message.name == "Scientist" else "💭"
                if message.name == "Judge":
                    speaker_emoji = "⚖️"
                    round_display = "FINAL JUDGMENT"
                else:
                    round_display = f"ROUND {current_round}"
                print(f"\n[{round_display}] {speaker_emoji} {message.name}:")
                print("-"*50)
                print(message.content.strip())
                print("-"*50 + "\n")
    print("\n✅ Debate complete. Check logs/debate_log_date_time.jsonl for full transcript\n")

if __name__ == "__main__":
    main()