from app.database import supabase
from app.llm import client
from datetime import datetime

async def summarize_session(session_id: str):
    events = (
        supabase.table("session_events")
        .select("content")
        .eq("session_id", session_id)
        .execute()
    )

    if not events.data:
        return

    conversation = "\n".join(e["content"] for e in events.data)

    prompt = f"Summarize this conversation:\n{conversation}"

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response.choices[0].message.content

    supabase.table("sessions").update({
        "summary": summary,
        "end_time": datetime.utcnow().isoformat()
    }).eq("session_id", session_id).execute()
