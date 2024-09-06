from uuid import UUID

from fastapi import APIRouter, Depends
from ...application.use_cases.create_message import CreateMessageUseCase
from ...application.use_cases.update_message import UpdateMessageUseCase
from ...application.use_cases.delete_message import DeleteMessageUseCase
from ...application.use_cases.read_message import ReadMessageUseCase
from ...domain.entities import Message
from ...infrastructure.repositories.in_memory_repository import (
    InMemoryMessageRepository,
)


message_router = APIRouter()


# Create repository as a singleton dependency
def get_message_repository():
    return InMemoryMessageRepository()


# Create use case dependencies
def get_create_message_use_case(repo=Depends(get_message_repository)):
    return CreateMessageUseCase(repo)


def get_update_message_use_case(repo=Depends(get_message_repository)):
    return UpdateMessageUseCase(repo)


def get_delete_message_use_case(repo=Depends(get_message_repository)):
    return DeleteMessageUseCase(repo)


def get_read_message_use_case(repo=Depends(get_message_repository)):
    return ReadMessageUseCase(repo)


@message_router.post("/", response_model=Message)
def create_message(
    content: str, use_case: CreateMessageUseCase = Depends(get_create_message_use_case)
):
    return use_case.execute(content)


@message_router.put("/{message_id}", response_model=Message)
def update_message(
    message_id: UUID,
    content: str,
    use_case: UpdateMessageUseCase = Depends(get_update_message_use_case),
):
    return use_case.execute(message_id, content)


@message_router.delete("/{message_id}", response_model=bool)
def delete_message(
    message_id: UUID,
    use_case: DeleteMessageUseCase = Depends(get_delete_message_use_case),
):
    return use_case.execute(message_id)


@message_router.get("/{message_id}", response_model=Message)
def get_message(
    message_id: UUID, use_case: ReadMessageUseCase = Depends(get_read_message_use_case)
):
    return use_case.execute(message_id)
