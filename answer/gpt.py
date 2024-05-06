import requests
import json

URL = 'https://ollamaunyang.kro.kr/api/generate'

def ask(problem):
    # prompt = {
    #     'model': 'llama3',
    #     'prompt': "내가 한국어로 질문을 줄게, 앞으로는 한국어로만 말하고 한국어로 대답하면 돼. 이제 다음 질문에 답해줘: " + problem,
    # }
    prompt = {
        'model': 'mistral',
        'prompt': problem,
    }
    response = _get_post_response(URL, prompt)
    answer = _process_text(response.text)
    return answer

def _get_post_response(URL, params):
    return requests.post(URL, json=params)

def _process_text(response_text):
    # print(response_text)
    responses = response_text.strip().split('\n')
    answer = ''
    for token in responses:
        answer += json.loads(token)['response']
    return answer

if __name__ == "__main__":
    while True:
        prompt = input(">>> ")
        print(ask(prompt))