import uuid
from typing import Optional
from ...domain.entities import Message
from ...domain.repositories import MessageRepository


class ReadMessageUseCase:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def execute(self, message_id: uuid.UUID) -> Optional[Message]:
        # Fetch the message by its ID
        return self.repository.get_message(message_id)
