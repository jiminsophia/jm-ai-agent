from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chatbot_response(user_message: str): 
    #OpenAI의 gpt-4.1-nano 모델 사용하여 응닶 생성

    result= client.responses.create(model="gpt-4.1-nano", input=user_message)
    return result

if __name__ == "__main__": 
    #이전 대화를 기억하지 못하는 챗봇
    
    while True:
        user_message= input("메시지: ")
        if user_message.lower() == "exit":
            print("대화를 종료합니다")
            break
        
        result= chatbot_response(user_message)
        print("챗봇: " + result.output_text)