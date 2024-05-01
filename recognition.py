import time
import os
import speech_recognition as sr
from pydub import AudioSegment
# from playsound import playsound

file_name = 'https://example.com/audio_file.wav'

def speech_recognition(audio_file):
    try:
        recognizer = sr.Recognizer()
        recognized_text = recognizer.recognize_google(audio_file, language='ko-KR')
        # print('[사용자] '+ text)
        return recognized_text
    except sr.UnknownValueError:
        print('인식 실패') 
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e)) #API key Error

def answer(text):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(file_name)
    # playsound(file_name)
    with audio_file as source:
        audio = recognizer.record(source)

if __name__ == '__main__':
    r = sr.Recognizer()
    # listen(recognizer, audio)
    with sr.WavFile("recorded2.wav") as source:
        audio_file = r.record(source)
    print(speech_recognition(audio_file))
