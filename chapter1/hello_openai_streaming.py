from openai import OpenAI
import rich

client = OpenAI()
default_model = 'gpt-4.1-nano'

def stream_chat_completion(prompt, model):
    # chat.completion API를 사용한 스트리밍 응답 함수

    stream = client.chat.completions.create(
        model = model, 
        messages = [{"role" : "user", "content" : "prompt"}], 
        max_completion_tokens= 200,
        stream = True   # 스트림 모드 활성화
    )

    for chunk in stream: # 응답 청크를 하나씩 처리
        content = chunk.choices[0].delta.content
        if content is not None: 
            print(content, end="")

def stream_response(prompt, model) :
    # 새로운 리스폰스 API를 사용한 스트리밍 함수 (컨텍스트 매니저로 스트림 관리)

    with client.responses.stream(model = model, input = prompt) as stream: 
        for event in stream:    #스트림에서 발생하는 각 이벤트 처리
            if "output_text" in event.type:     #텍스트 출력 이벤트인 경우
                rich.print(event)
    rich.print(stream.get_final_response())

if __name__ == "__main__" :
    stream_chat_completion("스트리밍이 뭔가요?", default_model)
    # stream_response("점심 메뉴 추천해주세요.", default_model)
