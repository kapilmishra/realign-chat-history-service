import uuid

from fastapi import APIRouter, Depends
from ...application.use_cases.create_message import CreateMessageUseCase
from ...application.use_cases.update_message import UpdateMessageUseCase
from ...application.use_cases.delete_message import DeleteMessageUseCase
from ...application.use_cases.read_message import ReadMessageUseCase
from ...domain.entities import Message
from ...infrastructure.repositories.in_memory_repository import InMemoryMessageRepository

# Initialize the in-memory repository
message_repository = InMemoryMessageRepository()

message_router = APIRouter()


@message_router.post("/", response_model=Message)
def create_message(content: str):
    use_case = CreateMessageUseCase(repository=message_repository)
    return use_case.execute(content)


@message_router.put("/{message_id}", response_model=Message)
def update_message(message_id: uuid.UUID, content: str):
    use_case = UpdateMessageUseCase(repository=message_repository)
    return use_case.execute(message_id, content)


@message_router.delete("/{message_id}",response_model=bool)
def delete_message(message_id: uuid.UUID):
    use_case = DeleteMessageUseCase(repository=message_repository)
    return use_case.execute(message_id)


@message_router.get("/{message_id}", response_model=Message)
def get_message(message_id: uuid.UUID):
    use_case = ReadMessageUseCase(repository=message_repository)
    return use_case.execute(message_id)
