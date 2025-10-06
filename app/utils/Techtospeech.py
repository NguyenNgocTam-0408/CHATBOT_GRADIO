import speech_recognition as sr

def speech_to_text(audio_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data, language="vi-VN")
            return text
        except sr.UnknownValueError:
            return "Xin lỗi, tôi không nghe rõ bạn nói gì."
        except sr.RequestError:
            return "Lỗi khi kết nối dịch vụ nhận diện giọng nói."
