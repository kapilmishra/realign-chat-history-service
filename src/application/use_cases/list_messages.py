import uuid
from typing import List

from ...domain.entities import Message
from ...domain.repositories import MessageRepository
from datetime import datetime


class ListMessageUseCase:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def execute(self) -> list[Message]:
        return self.repository.get_message_list()
