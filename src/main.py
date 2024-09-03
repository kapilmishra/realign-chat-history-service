from fastapi import FastAPI
from src.interfaces.api.message_router import message_router
from src.interfaces.api.conversation_router import conversation_router

app = FastAPI()

app.include_router(message_router,  prefix="/messages",)
app.include_router(conversation_router, prefix="/conversations")