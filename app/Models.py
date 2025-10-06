import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

# def call_gemini(prompt: str) -> str:
#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"Khong goi duoc API key gemini {e}"


def stream_gemini_response(prompt: str):
    """ cái này là trả về theo từng luồng """
    try:
        stream=model.generate_content(prompt,stream= True)
        for chunk in stream:
            text= chunk.text or ""
            if text.strip():
                yield text
    except Exception as e:
        yield f"not connect gemini {e}"
