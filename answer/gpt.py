import requests
import json

URL = 'https://ollamaunyang.kro.kr/api/generate'
model_name = 'llama3'
last_context = []

def ask(problem):
    # prompt = {
    #     'model': 'llama3',
    #     'prompt': "내가 한국어로 질문을 줄게, 앞으로는 한국어로만 말하고 한국어로 대답하면 돼. 이제 다음 질문에 답해줘: " + problem,
    # }
    prompt = {
        'model': model_name,
        'prompt': "내가 한국어로 질문을 줄게, 앞으로는 한국어로만 말하고 한국어로 대답하면 돼. 질문을 하는 사람은 한국에 사는 고등학생이야. 질문을 하는 사람에 맞춰서 잘 대답해줘. 이제 다음 질문에 답해줘: " + problem,
        'context': last_context,
    }
    try:
        response = _get_post_response(URL, prompt)
        answer = _process_text(response.text)
    except:
        answer = "오류 발생!"
    return answer

def _get_post_response(URL, params):
    return requests.post(URL, json=params)

def _process_text(response_text):
    global last_context
    # print(response_text)
    responses = response_text.strip().split('\n')
    answer = ''
    for response in responses:
        word = json.loads(response)
        answer += word['response']
        if 'context' in word:
            last_context = word['context']
    return answer

def _change_model(demanded_model):
    global model_name 
    global last_context
    model_name = demanded_model
    print("Current Model: " + model_name)
    last_context = []
    return


if __name__ == "__main__":
    while True:
        prompt = input(">>> ")
        if prompt == '':
            continue
        elif prompt[0] == '/':
            if prompt[1] == 'c':
                _change_model(prompt[2:].strip())
            elif prompt[1] == 'm':
                print("Current Model: " + model_name)
            elif prompt[1] == 'l':
                print(last_context)
        else:
            print(ask(prompt))