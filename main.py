import speech_recognition as sr

# 음성 인식기 생성
r = sr.Recognizer()

# 마이크로부터 음성 입력 받기
with sr.Microphone() as source:
    print("말씀해주세요...")
    while True:
        try:
            # 마이크로부터 음성 수신
            audio = r.listen(source)
            # 음성을 텍스트로 변환
            text = r.recognize_google(audio, language='ko-KR')
            print("인식된 텍스트: " + text)
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
        except sr.RequestError as e:
            print("음성 인식 서비스에 접근할 수 없습니다; {0}".format(e))
