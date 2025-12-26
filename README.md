# Realtime AI Backend (WebSockets + Supabase)

## 📌 Overview
This project implements a **real-time conversational AI backend** using **FastAPI**, **WebSockets**, **LLM streaming**, and **Supabase (PostgreSQL)**.  
It demonstrates core backend engineering patterns such as:

- Real-time bi-directional communication
- Streaming AI responses with low latency
- Asynchronous data persistence
- Session-based state management
- Post-session automation using background tasks

The project is intentionally built with **minimal UI** to focus on backend architecture and correctness.

---

## 🏗️ Architecture Overview

Frontend (HTML + JS)
│
│ WebSocket
▼
FastAPI WebSocket Server
│
├── Session State (in-memory)
├── LLM Streaming (OpenAI API)
├── Event Logging (Supabase)
│
▼
PostgreSQL (Supabase)
│
└── Background Task → Session Summary (LLM)

yaml
Copy code

---

## ⚙️ Tech Stack

- **Backend Framework**: FastAPI (async)
- **Realtime Communication**: WebSockets
- **LLM Provider**: OpenAI API (streaming responses)
- **Database**: Supabase (PostgreSQL)
- **Environment Management**: python-dotenv
- **Frontend**: Simple HTML + JavaScript

---

## 📂 Project Structure

real-time-ai-backend/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── websocket.py # WebSocket session handling
│ ├── llm.py # LLM streaming logic
│ ├── database.py # Supabase client
│ ├── background.py # Post-session summarization
│
├── frontend/
│ └── index.html # Simple WebSocket frontend
│
├── requirements.txt
├── .env # Environment variables (not committed)
├── .gitignore
└── README.md

pgsql
Copy code

---

## 🗄️ Database Schema (Supabase)

### 1️⃣ `sessions` table
```sql
CREATE TABLE sessions (
  session_id TEXT PRIMARY KEY,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  summary TEXT
);
2️⃣ session_events table
sql
Copy code
CREATE TABLE session_events (
  id SERIAL PRIMARY KEY,
  session_id TEXT,
  event_type TEXT,
  content TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
🚀 Setup Instructions (Windows)
1️⃣ Clone the repository
bash
Copy code
git clone https://github.com/Lucky-astro/real-time-ai-backend.git
cd real-time-ai-backend
2️⃣ Create and activate virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Configure environment variables
Create a .env file in the project root:

env
Copy code
OPENAI_API_KEY=your_openai_api_key
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_or_service_key
⚠️ Note: The .env file is intentionally excluded from GitHub.

▶️ Running the Application
Start the backend server
bash
Copy code
uvicorn app.main:app --reload
You should see:

nginx
Copy code
Uvicorn running on http://127.0.0.1:8000
Open the frontend
Open the file directly in your browser:

bash
Copy code
frontend/index.html
🧪 How to Test the System
1️⃣ Basic WebSocket Test
Open frontend

Type:

nginx
Copy code
hello
Observe real-time AI response streaming

2️⃣ Multi-turn Conversation Test
pgsql
Copy code
My name is Lucky
What is my name?
The AI correctly remembers prior context.

3️⃣ Supabase Persistence Test
Check session_events table

Verify user messages are logged with timestamps

4️⃣ Post-Session Automation Test
Close or refresh the browser tab

Check sessions table

A concise AI-generated session summary is stored

🧠 Key Design Choices
WebSockets over HTTP: Enables low-latency, bi-directional streaming

Async FastAPI: Non-blocking I/O for scalability

Event-based Persistence: Granular session logging

Graceful Error Handling: AI failures do not crash WebSocket sessions

Minimal Frontend: Focus on backend correctness over UI

⚠️ Notes on OpenAI API Usage
OpenAI API requires active billing

If quota is exceeded, the backend:

Handles the error gracefully

Keeps the WebSocket connection alive

This behavior is intentional and production-safe

✅ Assignment Requirements Mapping
Requirement	Status
WebSocket endpoint	✅
Streaming LLM responses	✅
Conversation state management	✅
Supabase persistence	✅
Event logging	✅
Post-session summarization	✅

📌 Conclusion
This project demonstrates a production-style real-time AI backend with proper async design, state management, persistence, and automation.
It is suitable for internship and junior backend engineering evaluations.

👤 Author
Lucky (Lakshmikar Dadisetty)
GitHub: https://github.com/Lucky-astro

