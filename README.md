# 💼 AI Interview Coach (Multi-Agent System using LangGraph)

## 🚀 Overview
This project is a multi-agent AI system that helps improve interview answers.  
It uses LangGraph to orchestrate multiple agents that evaluate, critique, and improve responses.

---

## 🧠 Architecture

The system consists of 3 AI agents:

1. **Evaluator Agent**
   - Analyzes the answer
   - Gives a score out of 10 with reasoning

2. **Feedback Agent**
   - Provides actionable feedback
   - Suggests improvements

3. **Improver Agent**
   - Rewrites the answer in a better, structured way

---
## 🔀 Workflow
User Input
↓
Evaluator Agent
↓
(If score is low)
↓
Feedback Agent → Improver Agent → Final Output
↓
(If score is high)
↓
END

---

## ⚙️ Tech Stack

- Python
- LangGraph
- LangChain
- OpenRouter (Free LLM API)
- LLaMA 3 (8B Instruct)

---

## 📂 Project Structure
ai-interview-coach/
│── app.py
│── llm.py
│── agents/
│ ├── evaluator.py
│ ├── feedback.py
│ ├── improver.py
│── requirements.txt
│── .env

---

## 🔑 Setup

1. Clone the repo

```bash
git clone <your-repo-link>
cd ai-interview-coach
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

3. Add your API Key in .env

OPENROUTER_API_KEY=your_key_here

4. Run the Project

```bash
python app.py
```

---
