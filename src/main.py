import logging
import sys
import time

from fastapi import FastAPI, Request
from src.interfaces.api.message_router import message_router
from src.interfaces.api.conversation_router import conversation_router

app = FastAPI()

app.include_router(
    message_router,
    prefix="/message",
    tags=["Message"]
)

app.include_router(
    conversation_router,
    prefix="/conversation",
    tags=["Conversation"]
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

logger.info('API is starting up')