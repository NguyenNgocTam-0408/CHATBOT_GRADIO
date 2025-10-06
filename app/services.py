from google import genai

from .Models import stream_gemini_response

def generate_response_stream(user_message: str) -> str:
    prompt = f"Người dùng: {user_message}\nTrợ lý:"
    for partial_text in stream_gemini_response(prompt):
        yield partial_text
# def transcribe_audio_with_gemini(audio_path):
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     try:
#         with open(audio_path, "rb") as f:
#             audio = {"mime_type": "audio/wav", "data": f.read()}
#         response = model.generate_content(
#             [audio, "Hãy chuyển đoạn giọng nói này thành văn bản tiếng Việt."]
#         )
#         return response.text.strip()
#     except Exception as e:
#         print("Lỗi chuyển giọng nói:", e)
#         return None