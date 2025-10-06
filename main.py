from turtledemo.penrose import start

import uvicorn
from django_migration_linter import analyse_sql_statements
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import threading

from app.router import router as chat_router
from frontend import  chat_ui
from frontend.chat_ui import start_ui

app = FastAPI(title="Gemini Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
async def root():
    return {"message": "✅ Gemini Chatbot API đang hoạt động!"}


def run_fastapi():
    """Chạy FastAPI (không bật reload vì đang trong thread phụ)"""
    uvicorn.run(app, host="127.0.0.1", port=8000)


def run_gradio():
    """Chạy giao diện Gradio"""
    start_ui()


if __name__ == "__main__":
    # Dùng 2 thread song song
    t1 = threading.Thread(target=run_fastapi)
    t2 = threading.Thread(target=run_gradio)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
