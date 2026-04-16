# Self-Learning Support Agent

An AI-powered customer support agent that improves its responses over time by learning from past mistakes using a feedback-driven memory system.

---

## 🚀 Overview

Most AI agents can remember past interactions, but they don’t actually *learn* from them.

This project demonstrates a simple but powerful idea:

> Memory alone doesn’t create learning — feedback does.

Instead of just storing conversations, this agent:
- Identifies poor responses
- Stores them as "failures"
- Uses those failures to improve future responses

---

## 🧠 How It Works

### Core Flow

User Input → Agent → Response  
                 ↓  
            Feedback (good/bad)  
                 ↓  
            Memory Store  
                 ↓  
        Memory Retrieval  
                 ↓  
        Improved Response  

---

## 🔁 Learning Loop

1. User asks a question  
2. Agent generates a response  
3. Response is marked as **good** or **bad**  
4. Bad responses are stored with a lesson  
5. On similar queries, the agent:
   - Retrieves past failures  
   - Avoids repeating mistakes  
   - Generates a better response  

---

## 💡 Example

### First Attempt (No Learning)

User: I didn’t get my refund
Agent: Please contact support.


### Second Attempt (After Learning)

User: I didn’t get my refund
Agent:

Check your order confirmation email
Verify refund status in your account
Contact support with your order ID
Expected processing time is 5–7 days

---

## 🛠️ Tech Stack

- Python
- Groq API (LLM)
- Custom memory system (inspired by Hindsight)

---

## 📂 Project Structure


.
├── main.py # Entry point
├── agent.py # LLM interaction + learning logic
├── memory.py # Memory storage and retrieval
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository


git clone https://github.com/your-username/self-learning-support-agent.git

cd self-learning-support-agent


---

### 2. Install dependencies


pip install -r requirements.txt


---

### 3. Add API Key

Create a `.env` file:


GROQ_API_KEY=your_api_key_here


---

### 4. Run the project


python main.py


---

## 🧪 How to Test Learning

1. Ask a question:

I didn’t get my refund


2. Mark response as:

bad


3. Ask the same question again

4. Observe improved response

---

## 🎯 Key Insights

- Memory alone is not enough for learning
- Feedback is critical for behavior change
- Agents must be forced to improve, not just recall
- Simple systems can demonstrate powerful learning concepts

---

## ⚠️ Limitations

- Feedback is manually provided (not fully automated)
- Memory is stored locally (not persistent across sessions)
- No advanced semantic search yet

---

## 🔮 Future Improvements

- Add semantic retrieval (vector search)
- Automate feedback using evaluation models
- Build a UI for better interaction

---
