import os
from dotenv import load_dotenv
from openai import OpenAI

# .env에서 환경변수 로드
load_dotenv()
api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key = api_key) # openai 클라이언트 초기화

def get_chat_completion(prompt, model = 'gpt-4.1-nano') :
    # openai 챗컴플리션 api 사용하여 api 응답 받는 함수

    # 챗컴플리션 api 호출
    response = client.chat.completions.create(
        model = model, 
        messages = [
            {"role" : "system", 
             "content" : "당신은 친절하고 도움이 되는 AI 비서입니다."}, 
            {"role" : "user", 
             "content" : prompt}
        ],
        max_completion_tokens = 100
    )
    # 응답 텍스트 변환
    return response.choices[0].message.content

if __name__ == "__main__" :
    # 사용자 입력받기
    user_prompt = input("AI에게 물어볼 질문을 입력하세요: ")
    # AI 응답받기
    response = get_chat_completion(user_prompt)

    print("\nAI 응답: ")
    print(response)

