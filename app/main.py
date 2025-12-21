from fastapi import FastAPI
from app.websocket import session_ws
from fastapi import WebSocket

app = FastAPI()   # 👈 THIS LINE IS REQUIRED

@app.websocket("/ws/session/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await session_ws(websocket, session_id)
