from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Session(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_seconds: Optional[int] = None
    summary: Optional[str] = None


class SessionEvent(BaseModel):
    session_id: str
    event_type: str
    content: str
    created_at: Optional[datetime] = None
