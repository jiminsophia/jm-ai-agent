from openai import OpenAI

client= OpenAI()

#previous_response_id 파라미터 추가
def chatbot_response(user_message: str, previous_resoonse_id= None): 
    result= client.responses.create(
        model= "gpt-4.1-nano", 
        input= user_message, 
        previous_response_id= previous_resoonse_id
    )
    return result

if __name__== "__main__": 
    #이전 대화를 기억하는 챗봇
    previous_response_id= None
    
    while True:
        user_message= input("메시지: ")
        if user_message.lower() == "exit": 
            print("대화를 종료합니다.")
            break
        
        #이전 대화의 id값을 추가로 넘기기
        result= chatbot_response(user_message, previous_response_id)
        previous_response_id= result.id
        print(result.output_text)
