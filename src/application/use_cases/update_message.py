import uuid
from typing import Optional
from ...domain.entities import Message
from ...domain.repositories import MessageRepository
from datetime import datetime


class UpdateMessageUseCase:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def execute(self, message_id: uuid.UUID, content: str) -> Optional[Message]:
        # Fetch the existing message
        message = self.repository.get_message(message_id)
        if message is None:
            return None

        # Update the message content and timestamp
        message.content = content
        message.updated_at = datetime.now()

        # Persist the changes
        updated_message = self.repository.update_message(message_id, content)
        return updated_message
