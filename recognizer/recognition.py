import speech_recognition as sr

# file_name = 'https://example.com/audio_file.wav'

def text_recognition(audio_file_path):
    try:
        recognizer = sr.Recognizer()
        with sr.WavFile(audio_file_path) as source:
            audio_file = recognizer.record(source)
        recognized_text = recognizer.recognize_google(audio_file, language='ko-KR')
        # print('[사용자] '+ text)
        return recognized_text
    except sr.UnknownValueError:
        # print('인식 실패') 
        return "인식 실패"
    except sr.RequestError as e:
        # print('요청 실패 : {0}'.format(e)) #API key Error
        return f'요청 실패: {e}'

# 대답하는거는 나중에 추가하면 될 듯
# def answer(text):
#     recognizer = sr.Recognizer()
#     audio_file = sr.AudioFile(file_name)
#     # playsound(file_name)
#     with audio_file as source:
#         audio = recognizer.record(source)
import os

if __name__ == '__main__':
    # print(text_recognition("test.wav"))
    print(os.getcwd())