import uuid
from typing import Optional, List
from ...domain.entities import Conversation
from ...domain.repositories import ConversationRepository


class ListConversationUseCase:
    def __init__(self, repository: ConversationRepository):
        self.repository = repository

    def execute(self) -> list[Conversation]:
        return self.repository.get_conversation_list()
