import uuid
from typing import Optional
from ...domain.entities import Message, Conversation
from ...domain.repositories import ConversationRepository, MessageRepository
from datetime import datetime


class AppendMessageUseCase:
    def __init__(self, conversation_repository: ConversationRepository, message_repository: MessageRepository):
        self.conversation_repository = conversation_repository
        self.message_repository = message_repository

    def execute(self, conversation_id: uuid.UUID, content: str) -> Optional[Conversation]:
        # Fetch the existing conversation
        conversation = self.conversation_repository.get_conversation(conversation_id)
        if conversation is None:
            return None

        # Create a new message
        new_message = Message(id=uuid.uuid4(), content=content, created_at=datetime.now(), updated_at=datetime.now())

        # Save the message in the repository (if needed)
        saved_message = self.message_repository.create_message(new_message)

        # Append the message to the conversation
        updated_conversation = self.conversation_repository.append_message(conversation_id, saved_message)

        # Update the conversation's updated_at timestamp
        if updated_conversation:
            updated_conversation.updated_at = datetime.now()

        return updated_conversation
