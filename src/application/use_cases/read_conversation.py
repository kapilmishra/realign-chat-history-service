import uuid
from typing import Optional
from ...domain.entities import Conversation
from ...domain.repositories import ConversationRepository


class ReadConversationUseCase:
    def __init__(self, repository: ConversationRepository):
        self.repository = repository

    def execute(self, conversation_id: uuid.UUID) -> Optional[Conversation]:
        # Fetch the conversation by its ID
        return self.repository.get_conversation(conversation_id)
