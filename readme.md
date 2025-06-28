# 🧠 Multi-Agent Debate System

This project simulates a structured debate between two AI agents — a **Scientist** and a **Philosopher** — on a user-defined topic. The debate proceeds in turns, with a final **Judge** agent summarizing and deciding the winner.

Built with:
- LangGraph
-  Google Gemini (via LangChain)
-  Custom modular nodes (agents, memory, judge, logging)

---

## 🚀 Features

- 💬 Turn-based debate between Scientist and Philosopher
- 🧠 Intelligent prompting via LangChain & Gemini
- 📚 Stateful memory tracking each agent’s past arguments
- ⚖️ Final judgment with summary and declared winner
- 📄 Logs saved as `.jsonl` for analysis or replay
- ✅ Clean CLI output per round

---

##  Project Structure
```bash
multi_agent_debate/
│
├── main.py # Entry point: starts the debate
├── logs/
│ └── debate_log_<timestamp>.jsonl # Debate logs per run
├── src/
│ ├── dag/
│ │ └── debate_dag.py # LangGraph DAG logic
│ ├── agents/
│ │ ├── agent_a.py # Prompt template (Scientist)
│ │ ├── agent_b.py # Prompt template (Philosopher)
│ ├── nodes/
│ │ ├── agent_a_node.py # Agent A inference logic
│ │ ├── agent_b_node.py # Agent B inference logic
│ │ ├── memory_node.py # Memory updater
│ │ └── judge_node.py # Judge logic
│ ├── utils.py       # Gemini LLM call
│ │ 
│ ├── logger.py # JSONL logger
│ └──user_input.py # Topic input
└── README.md
```

---

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/sawanrepo/MULTI_AGENT_DEBATE.git
   cd MULTI_AGENT_DEBATE
   ```

2. **Create Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows  source venv/bin/activate for mac /linuix
```

3. **Install dependencies**
``` bash
pip install -r requirements.txt
```

4 .**Set your Google API key**
Create a .env file:
```bash
GOOGLE_API_KEY=your_gemini_api_key
```
5 **Run the Debate**
```bash
python main.py
```
`*You'll be prompted to enter a topic.*`

`*The Scientist and Philosopher take turns.*`

`*A Judge concludes the debate with a verdict.*`

##  Logs
`*All debates are saved in the logs/ folder as .jsonl*`

`*Can be parsed, analyzed, or visualized later*`

`*Each message includes: round, role, content, topic*`

## 🗺️ Debate Flow Diagram (LangGraph)

```mermaid
flowchart TD
    Start([Start]) --> A[👨‍🔬 Agent A (Scientist)]
    A --> M1[[🧠 Update Memory]]
    M1 --> Cond{🔁 Round Check}
    
    Cond -- Round < 8 --> B[💭 Agent B (Philosopher)]
    B --> M2[[🧠 Update Memory]]
    M2 --> Cond

    Cond -- Round ≥ 8 --> J[⚖️ Judge]
    J --> End([End])
```
