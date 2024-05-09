import os
import sys
from flask import request, Blueprint
from recognizer import recognition, encoder
from answer import gpt

Audio = Blueprint('Audio', __name__, url_prefix='/audio')

ROOT_PATH = os.getcwd()
RECORD_PATH = os.path.join(ROOT_PATH, 'files', 'recorded_audio')
LOSSLESS_PATH = os.path.join(ROOT_PATH, 'files', 'lossless_audio')
PLATFORM = sys.platform
FFMPEG_PATH = os.path.join(ROOT_PATH, 'ffmpeg', 'bin', 'ffmpeg.exe')

if not os.path.exists(RECORD_PATH):
    os.mkdir(RECORD_PATH)
if not os.path.exists(LOSSLESS_PATH):
    os.mkdir(LOSSLESS_PATH)

@Audio.route('/recognize_audio', methods=['POST'])
def recognize_audio():
    if 'audio' not in request.files:
        return '음성 파일이 없습니다.', 400
    audio_file = request.files['audio']
    if audio_file.filename == '':
        return '음성 파일이 선택되지 않았습니다.', 400
    
    count = len(os.listdir(RECORD_PATH))    
    audio_path = os.path.join(RECORD_PATH, f'({count}) {audio_file.filename}')
    audio_file.save(audio_path)

    # 여기서 음성 파일을 처리하고 텍스트로 변환하는 코드 추가
    RESULT_PATH = os.path.join(ROOT_PATH, 'files', 'lossless_audio')
    if PLATFORM == 'win32':
        converted_audio_path = encoder.convert_aac_to_wav(audio_path, RESULT_PATH, FFMPEG_PATH) # 리눅스에서는 불필요함
    else:
        converted_audio_path = encoder.convert_aac_to_wav(audio_path, RESULT_PATH)
    recognized_text = recognition.text_recognition(converted_audio_path)

    return recognized_text, 200

if __name__ == '__main__':
    print('a')