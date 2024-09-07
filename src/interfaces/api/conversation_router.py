from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from ...application.use_cases.create_conversation import CreateConversationUseCase
from ...application.use_cases.list_conversation import ListConversationUseCase
from ...application.use_cases.update_conversation import UpdateConversationUseCase
from ...application.use_cases.delete_conversation import DeleteConversationUseCase
from ...application.use_cases.read_conversation import ReadConversationUseCase
from ...application.use_cases.append_message import AppendMessageUseCase
from ...infrastructure.repositories.in_memory_repository import (
    InMemoryConversationRepository,
    InMemoryMessageRepository,
)
from ...domain.entities import Conversation

conversation_router = APIRouter()


# Create repository as a singleton dependency
def get_conversation_repository():
    return InMemoryConversationRepository()


def get_message_repository():
    return InMemoryMessageRepository()


# Use case dependencies
def get_create_conversation_use_case(
    repo: InMemoryConversationRepository = Depends(get_conversation_repository),
):
    return CreateConversationUseCase(repo)


def get_update_conversation_use_case(
    repo: InMemoryConversationRepository = Depends(get_conversation_repository),
):
    return UpdateConversationUseCase(repo)


def get_delete_conversation_use_case(
    repo: InMemoryConversationRepository = Depends(get_conversation_repository),
):
    return DeleteConversationUseCase(repo)


def get_read_conversation_use_case(
    repo: InMemoryConversationRepository = Depends(get_conversation_repository),
):
    return ReadConversationUseCase(repo)


def get_list_conversation_use_case(
    repo: InMemoryConversationRepository = Depends(get_conversation_repository),
):
    return ListConversationUseCase(repo)


def get_append_message_use_case(
    conversation_repo: InMemoryConversationRepository = Depends(
        get_conversation_repository
    ),
    message_repo: InMemoryMessageRepository = Depends(get_message_repository),
):
    return AppendMessageUseCase(conversation_repo, message_repo)


# API Endpoints


@conversation_router.post("/", response_model=Conversation)
def create_conversation(
    title: str,
    use_case: CreateConversationUseCase = Depends(get_create_conversation_use_case),
):
    return use_case.execute(title)


@conversation_router.put("/{conversation_id}", response_model=Conversation)
def update_conversation(
    conversation_id: UUID,
    title: str,
    use_case: UpdateConversationUseCase = Depends(get_update_conversation_use_case),
):
    return use_case.execute(conversation_id, title)


@conversation_router.delete("/{conversation_id}", response_model=bool)
def delete_conversation(
    conversation_id: UUID,
    use_case: DeleteConversationUseCase = Depends(get_delete_conversation_use_case),
):
    return use_case.execute(conversation_id)


@conversation_router.get("/{conversation_id}", response_model=Conversation)
def read_conversation(
    conversation_id: UUID,
    use_case: ReadConversationUseCase = Depends(get_read_conversation_use_case),
):
    return use_case.execute(conversation_id)


@conversation_router.get("/list", response_model=List[Conversation])
def list_conversation(
    use_case: ListConversationUseCase = Depends(get_list_conversation_use_case),
):
    return use_case.execute()


@conversation_router.post(
    "/{conversation_id}/append-message", response_model=Conversation
)
def append_message_to_conversation(
    conversation_id: UUID,
    message_content: str,
    use_case: AppendMessageUseCase = Depends(get_append_message_use_case),
):
    return use_case.execute(conversation_id, message_content)
