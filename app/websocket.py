from fastapi import WebSocket
from datetime import datetime
from app.llm import stream_llm_response
from app.database import supabase
from app.background import summarize_session

async def session_ws(websocket: WebSocket, session_id: str):
    await websocket.accept()

    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    # Safe session insert
    try:
        supabase.table("sessions").insert({
            "session_id": session_id,
            "start_time": datetime.utcnow().isoformat()
        }).execute()
    except Exception as e:
        print("Session insert failed:", e)

    try:
        while True:
            user_text = await websocket.receive_text()

            # Safe event insert
            try:
                supabase.table("session_events").insert({
                    "session_id": session_id,
                    "event_type": "user",
                    "content": user_text
                }).execute()
            except Exception as e:
                print("Event insert failed:", e)

            messages.append({"role": "user", "content": user_text})

            await stream_llm_response(messages, websocket)

    except Exception as e:
        print("WebSocket disconnected:", e)

    finally:
        try:
            await summarize_session(session_id)
        except Exception as e:
            print("Summary failed:", e)
