import uuid

from ...domain.repositories import MessageRepository


class DeleteMessageUseCase:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def execute(self, message_id: uuid.UUID) -> bool:
        # Check if the message exists before attempting to delete
        message = self.repository.get_message(message_id)
        if message is None:
            return False

        # Delete the message
        self.repository.delete_message(message_id)
        return True
