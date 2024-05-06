from flask import Flask, request, render_template
import os
from recognizer import recognition, encoder
from answer import gpt

app = Flask(__name__)
DIR_PATH = os.getcwd()
FFMPEG_PATH = os.path.join(DIR_PATH, 'ffmpeg', 'bin', 'ffmpeg.exe')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/recognize_audio', methods=['POST'])
def recognize_audio():
    if 'audio' not in request.files:
        return '음성 파일이 없습니다.', 400
    audio_file = request.files['audio']
    if audio_file.filename == '':
        return '음성 파일이 선택되지 않았습니다.', 400

    # 음성 파일을 저장할 경로 설정
    SAVE_PATH = os.path.join(DIR_PATH, 'uploads')
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)
    
    audio_path = os.path.join(SAVE_PATH, audio_file.filename)
    audio_file.save(audio_path)

    # 여기서 음성 파일을 처리하고 텍스트로 변환하는 코드 추가
    RESULT_PATH = os.path.join(DIR_PATH, 'uploads', 'result.wav')
    converted_audio_path = encoder.convert_aac_to_wav(audio_path, RESULT_PATH, FFMPEG_PATH)
    recognized_text = recognition.text_recognition(converted_audio_path)

    return recognized_text, 200

@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()  # 클라이언트로부터 JSON 데이터 받기
    return gpt.ask(data['scripts'])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
    