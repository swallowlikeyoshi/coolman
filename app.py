from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return '음성 파일이 없습니다.', 400
    
    audio_file = request.files['audio']
    if audio_file.filename == '':
        return '음성 파일이 선택되지 않았습니다.', 400

    # 음성 파일을 저장할 경로 설정
    save_path = 'uploads'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    audio_path = os.path.join(save_path, audio_file.filename)
    audio_file.save(audio_path)

    # 여기서 음성 파일을 처리하고 텍스트로 변환하는 코드 추가
    print("asdf")

    return '음성 파일이 업로드되었습니다.', 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)