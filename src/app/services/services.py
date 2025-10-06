from src.app.Models.Models import stream_gemini_response

def generate_response_stream(user_message: str) -> str:
    prompt = f"Người dùng: {user_message}\nTrợ lý:"
    for partial_text in stream_gemini_response(prompt):
        yield partial_text
