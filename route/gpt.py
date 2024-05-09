from flask import Blueprint, request
from answer import gpt

LLM = Blueprint('llm', __name__, url_prefix='/llm')

# ! ollama API URL을 은닉하려면 질의를 서버에서 진행해야 함. !
@LLM.route('/question', methods=['POST'])
def answer():
    data = request.get_json()  # 클라이언트로부터 JSON 데이터 받기
    return gpt.ask(data['scripts'])