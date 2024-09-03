import uuid

from ...domain.entities import Conversation
from ...domain.repositories import ConversationRepository
from datetime import datetime


class CreateConversationUseCase:
    def __init__(self, repository: ConversationRepository):
        self.repository = repository

    def execute(self, title: str) -> Conversation:
        conversation = Conversation(id=uuid.uuid4(), title=title, created_at=datetime.now(), updated_at=datetime.now())
        return self.repository.create_conversation(conversation)
