def get_debate_topic() -> str:
    topic = input("Enter topic for debate: ").strip()
    if not topic:
        print("⚠️ Topic cannot be empty. Try again.")
        return get_debate_topic()
    return topic