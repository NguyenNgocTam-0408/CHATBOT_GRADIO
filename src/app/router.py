from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from src.app.services.services import generate_response_stream

router = APIRouter()

class Message(BaseModel):
    user_message: str

@router.post("/chat/stream")
async def chat_stream(msg: Message):
    def event_stream():
        for part in generate_response_stream(msg.user_message):
            yield part
    return StreamingResponse(event_stream(), media_type="text/plain")
