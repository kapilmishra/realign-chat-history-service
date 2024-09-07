import time

from fastapi import FastAPI, Request
from src.interfaces.api.message_router import message_router
from src.interfaces.api.conversation_router import conversation_router

app = FastAPI()

app.include_router(
    message_router,
    prefix="/messages",
)
app.include_router(conversation_router, prefix="/conversations")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
