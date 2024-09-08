from uuid import UUID
from typing import Optional, List

from ...domain.entities import Message, Conversation
from ...domain.repositories import MessageRepository, ConversationRepository


class InMemoryMessageRepository(MessageRepository):

    def __init__(self):
        self.messages = {}

    def create_message(self, message: Message) -> Message:
        self.messages[message.id] = message
        return message

    def update_message(self, message_id: UUID, content: str) -> Optional[Message]:
        if message_id in self.messages:
            self.messages[message_id].content = content
            return self.messages[message_id]
        return None

    def delete_message(self, message_id: UUID) -> None:
        if message_id in self.messages:
            del self.messages[message_id]

    def get_message(self, message_id: UUID) -> Optional[Message]:
        return self.messages.get(message_id)

    def get_message_list(self) -> List[Message]:
        return list(self.messages.values())


class InMemoryConversationRepository(ConversationRepository):

    def __init__(self):
        self.conversations = {}

    def create_conversation(self, conversation: Conversation) -> Conversation:
        self.conversations[conversation.id] = conversation
        return conversation

    def update_conversation(
        self, conversation_id: UUID, title: str
    ) -> Optional[Conversation]:
        if conversation_id in self.conversations:
            self.conversations[conversation_id].title = title
            return self.conversations[conversation_id]
        return None

    def delete_conversation(self, conversation_id: UUID) -> None:
        if conversation_id in self.conversations:
            del self.conversations[conversation_id]

    def get_conversation(self, conversation_id: UUID) -> Optional[Conversation]:
        return self.conversations.get(conversation_id)

    def get_conversation_list(self) -> List[Conversation]:
        return list(self.conversations.values())

    def append_message(
        self, conversation_id: UUID, message: Message
    ) -> Optional[Conversation]:
        if conversation_id in self.conversations:
            self.conversations[conversation_id].messages.append(message)
            return self.conversations[conversation_id]
        return None
