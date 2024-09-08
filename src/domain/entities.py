from uuid import UUID
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    id: UUID
    content: str
    created_at: datetime
    updated_at: Optional[datetime] = None


class Conversation(BaseModel):
    id: UUID
    title: str
    messages: List[Message] = []
    created_at: datetime
    updated_at: Optional[datetime] = None
