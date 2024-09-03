import uuid

from fastapi import APIRouter, Depends
from ...application.use_cases.create_conversation import CreateConversationUseCase
from ...application.use_cases.update_conversation import UpdateConversationUseCase
from ...application.use_cases.delete_conversation import DeleteConversationUseCase
from ...application.use_cases.read_conversation import ReadConversationUseCase
from ...application.use_cases.append_message import AppendMessageUseCase
from ...domain.entities import Message, Conversation
from ...infrastructure.repositories.in_memory_repository import InMemoryConversationRepository, \
    InMemoryMessageRepository

# Initialize the in-memory repositories
conversation_repository = InMemoryConversationRepository()
message_repository = InMemoryMessageRepository()

conversation_router = APIRouter()


@conversation_router.post("/", response_model=Conversation)
def create_conversation(title: str):
    use_case = CreateConversationUseCase(repository=conversation_repository)
    return use_case.execute(title)


@conversation_router.put("/{conversation_id}", response_model=Conversation)
def update_conversation(conversation_id: uuid.UUID, title: str):
    use_case = UpdateConversationUseCase(repository=conversation_repository)
    return use_case.execute(conversation_id, title)


@conversation_router.delete("/{conversation_id}", response_model=bool)
def delete_conversation(conversation_id: uuid.UUID):
    use_case = DeleteConversationUseCase(repository=conversation_repository)
    return use_case.execute(conversation_id)


@conversation_router.get("/{conversation_id}", response_model=Conversation)
def get_conversation(conversation_id: uuid.UUID):
    use_case = ReadConversationUseCase(repository=conversation_repository)
    return use_case.execute(conversation_id)


@conversation_router.post("/{conversation_id}/messages")
def append_message(conversation_id: uuid.UUID, content: str):
    use_case = AppendMessageUseCase(conversation_repository=conversation_repository,
                                    message_repository=message_repository)
    return use_case.execute(conversation_id, content)
