from fastapi import WebSocket
from app.database import supabase
from app.llm import stream_llm_response
from app.models import SessionEvent   # 👈 ADD THIS LINE HERE

async def session_ws(websocket: WebSocket, session_id: str):
    await websocket.accept()

    # Create session record
    supabase.table("sessions").insert({
        "session_id": session_id
    }).execute()

    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    try:
        while True:
            user_text = await websocket.receive_text()

            # Save user message
            supabase.table("session_events").insert({
                "session_id": session_id,
                "event_type": "user",
                "content": user_text
            }).execute()

            messages.append({"role": "user", "content": user_text})

            # Stream LLM response
            await stream_llm_response(messages, websocket)

    except Exception as e:
        print("WebSocket closed:", e)
