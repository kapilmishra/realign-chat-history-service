import uuid
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    id: uuid.UUID
    content: str
    created_at: datetime
    updated_at: Optional[datetime] = None


class Conversation(BaseModel):
    id: uuid.UUID
    title: str
    messages: List[Message] = []
    created_at: datetime
    updated_at: Optional[datetime] = None
