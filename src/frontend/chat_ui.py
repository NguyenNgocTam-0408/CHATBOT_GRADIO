import gradio as gr
import time
from src.app.services.services import generate_response_stream


def streaming_chat(message, history):
    partial = ""
    typing_speed = 0.035  # tốc độ hiển thị
    chunk_size = 8

    # Hiệu ứng "đang soạn"
    yield gr.ChatMessage(role="assistant", content="Đang soạn phản hồi...")

    time.sleep(0.5)

    # Nhận từng chunk từ API Gemini
    for chunk in generate_response_stream(message):
        for i in range(0, len(chunk), chunk_size):
            partial += chunk[i:i + chunk_size]

            # Gửi message từng phần (stream)
            yield gr.ChatMessage(role="assistant", content=partial)
            time.sleep(typing_speed)


def start_ui():
    gr.ChatInterface(
        fn=streaming_chat,
        title="🤖 Gemini Chatbot Streaming",
        description="Chatbot phản hồi tự nhiên như ChatGPT ✨",
        theme="soft",
    ).launch(server_port=7860)
