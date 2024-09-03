import uuid
from abc import ABC, abstractmethod
from typing import List, Optional

from .entities import Message, Conversation


class MessageRepository(ABC):
    @abstractmethod
    def create_message(self, message: Message) -> Message:
        pass

    @abstractmethod
    def update_message(self, message_id: uuid, content: str) -> Optional[Message]:
        pass

    @abstractmethod
    def delete_message(self, message_id: uuid) -> None:
        pass

    @abstractmethod
    def get_message(self, message_id: uuid) -> Optional[Message]:
        pass


class ConversationRepository(ABC):
    @abstractmethod
    def create_conversation(self, conversation: Conversation) -> Conversation:
        pass

    @abstractmethod
    def update_conversation(self, conversation_id: uuid, title: str) -> Optional[Conversation]:
        pass

    @abstractmethod
    def delete_conversation(self, conversation_id: uuid) -> None:
        pass

    @abstractmethod
    def get_conversation(self, conversation_id: uuid) -> Optional[Conversation]:
        pass

    @abstractmethod
    def append_message(self, conversation_id: uuid, message: Message) -> Optional[Conversation]:
        pass
