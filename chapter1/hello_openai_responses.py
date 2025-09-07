from openai import OpenAI
client = OpenAI()

def get_responses(prompt, model = 'gpt-5-nano'): 
    # 입력된 프롬프트에 대한 AI 응답을 받아오는 함수

    response = client.responses.create(
        model = model, # 사용 모델 지정
        tools = [{"type" : "web_search_preview"}],  # 웹 검색 도구 활성화
        input = prompt,   # 사용자 입력 전달
        # max_output_tokens= 50
    )
    return response.output_text # 텍스트 응답만 반환

if __name__ == '__main__' :
    prompt = """
https://platform.openai.com/docs/api-reference/responses/create
를 읽어서 리스폰스 API에 대해 요약 정리해주세요.
"""
    output = get_responses(prompt)
    print(output)