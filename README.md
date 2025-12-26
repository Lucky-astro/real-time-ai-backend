# Realtime AI Backend (WebSockets + Supabase)

## Overview

This project implements a **high-performance, asynchronous realtime AI backend** that simulates a live conversational session.  
The system demonstrates **production-grade backend patterns** including:

- Real-time bi-directional communication using **WebSockets**
- **Streaming LLM responses** for low-latency interaction
- **Conversation state management** across multiple turns
- **Asynchronous persistence** using Supabase (PostgreSQL)
- **Post-session automation** for AI-generated conversation summaries

A minimal frontend is included to easily test WebSocket connectivity and streaming behavior.

---

## Architecture Overview

**Flow:**

1. Client connects via WebSocket
2. User messages are sent in real time
3. LLM responses are streamed token-by-token
4. All events are logged to Supabase
5. On disconnect, the conversation is summarized and persisted

Frontend (HTML + JS)
⇅ WebSocket
FastAPI Backend
⇅ Async LLM Streaming
Supabase (Postgres)
⇢ Post-Session Summary Task

yaml
Copy code

---

## Tech Stack

- **Python 3.10+**
- **FastAPI** – async backend framework
- **WebSockets** – real-time communication
- **OpenAI API** – LLM streaming & analysis
- **Supabase (Postgres)** – persistence layer
- **HTML + JavaScript** – minimal frontend UI

---

## Project Structure

real-time-ai-backend/
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app & WebSocket endpoint
│ ├── websocket.py # Session & streaming logic
│ ├── llm.py # LLM streaming + tool handling
│ ├── database.py # Supabase client
│ ├── models.py # Session & event models
│ └── background.py # Post-session processing
│
├── frontend/
│ └── index.html # Simple WebSocket test UI
│
├── .gitignore
├── requirements.txt
├── README.md

pgsql
Copy code

---

## Supabase Database Schema

Run the following SQL in the **Supabase SQL Editor**:

```sql
-- Session metadata table
CREATE TABLE sessions (
    session_id TEXT PRIMARY KEY,
    user_id TEXT,
    start_time TIMESTAMP DEFAULT NOW(),
    end_time TIMESTAMP,
    duration_seconds INT,
    summary TEXT
);

-- Detailed event log table
CREATE TABLE session_events (
    id SERIAL PRIMARY KEY,
    session_id TEXT REFERENCES sessions(session_id),
    event_type TEXT,
    content TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
⚠️ Note: Disable Row Level Security (RLS) for development/testing.

Setup Instructions (Windows)
1. Clone Repository

Copy 
git clone <your-repo-url>
cd real-time-ai-backend
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3. Install Dependencies

pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the project root:

env
SUPABASE_URL=https://<your-project>.supabase.co
SUPABASE_KEY=<your-anon-public-key>
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
❗ Do NOT commit .env to GitHub.

Running the Backend

uvicorn app.main:app --reload
Expected output:

Uvicorn running on http://127.0.0.1:8000
Application startup complete.
Testing the Application
1. Backend Health Check
Open in browser:


http://127.0.0.1:8000/docs
Swagger UI confirms the backend is running.

2. WebSocket Chat Test (Frontend)
Open:

frontend/index.html
Type a message (e.g. Hello)

Click Send

Expected Behavior:

AI response streams token-by-token

WebSocket remains connected

Low-latency interaction

3. State Management Test
Send:


My name is Lucky
Then:


What is my name?
Expected Response:


Your name is Lucky
4. Supabase Verification
Check Supabase tables:

sessions
New row created per session

session_events
Chronological log of messages and AI responses

Complex LLM Interaction
This project demonstrates advanced LLM handling:

Streaming responses (token-by-token)

Conversation state preservation

Multi-turn contextual reasoning

Ready for tool/function calling extensions

Post-Session Processing
On WebSocket disconnect:

Conversation history is retrieved from Supabase

LLM generates a concise session summary

Summary, end time, and duration are saved to sessions

Key Design Decisions
WebSockets chosen for true real-time bi-directional communication

Async-first architecture for scalability

Event-level persistence enables replay, analytics, and auditing

Minimal frontend keeps focus on backend engineering

Security Notes
API keys stored in environment variables

.env excluded via .gitignore

Supabase anon key used with controlled permissions

Future Enhancements
Tool / function calling

Authentication & user management

Advanced routing based on user intent

Deployment with Docker & cloud hosting

Author
Lakshmikar Dadisetty

License
This project is provided for educational and evaluation purposes.



