import uuid

from ...domain.entities import Message
from ...domain.repositories import MessageRepository
from datetime import datetime


class CreateMessageUseCase:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def execute(self, content: str) -> Message:
        message = Message(id=uuid.uuid4(), content=content, created_at=datetime.now(), updated_at=datetime.now())
        return self.repository.create_message(message)
