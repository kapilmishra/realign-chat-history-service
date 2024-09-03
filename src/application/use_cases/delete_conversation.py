from uuid import UUID

from ...domain.repositories import ConversationRepository


class DeleteConversationUseCase:
    def __init__(self, repository: ConversationRepository):
        self.repository = repository

    def execute(self, conversation_id: UUID) -> bool:
        # Check if the conversation exists before attempting to delete
        conversation = self.repository.get_conversation(conversation_id)
        if conversation is None:
            return False

        # Delete the conversation
        self.repository.delete_conversation(conversation_id)
        return True
