import uuid
from typing import Optional
from ...domain.entities import Conversation
from ...domain.repositories import ConversationRepository
from datetime import datetime


class UpdateConversationUseCase:
    def __init__(self, repository: ConversationRepository):
        self.repository = repository

    def execute(self, conversation_id: uuid.UUID, title: str) -> Optional[Conversation]:
        # Fetch the existing conversation
        conversation = self.repository.get_conversation(conversation_id)
        if conversation is None:
            return None

        # Update the conversation title and timestamp
        conversation.title = title
        conversation.updated_at = datetime.now()

        # Persist the changes
        updated_conversation = self.repository.update_conversation(conversation_id, title)
        return updated_conversation
