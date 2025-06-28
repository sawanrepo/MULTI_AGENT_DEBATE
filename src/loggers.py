import os
import json
import time 
timestamp = time.strftime("%Y%m%d_%H%M%S")
LOG_FILE = f"logs/debate_log{timestamp}.jsonl"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_message(state, message_obj, is_judge=False):
    log_entry = {
        "type": "judge" if is_judge else "agent",
        "round": state["round"] if not is_judge else None,
        "speaker": getattr(message_obj, "name", "Unknown"),
        "content": getattr(message_obj, "content", str(message_obj)).strip(),
        "topic": state.get("topic", ""),
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")