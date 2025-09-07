import asyncio
import os

from openai import AsyncOpenAI
from anthropic import AsyncAnthropic

openai_client = AsyncOpenAI(api_key = os.environ.get("OPENAI_API_kEY"))
claude_client = AsyncAnthropic(api_key = os.environ.get("ANTHROPIC_API_KEY"))

async def call_async_openai(prompt: str, model: str = "gpt-4.1-nano") -> str:
    # await 을 사용해 비동기적으로 API 응답을 기다림

    response = await openai_client.chat.completions.create(
        model= model, 
        messages= [{"role": "user", "content": prompt}], 
        max_completion_tokens= 100
    )
    return response.choices[0].message.content


async def call_async_claude(prompt: str, model: str = "claude-3-5-haiku-latest") -> str:
    #await 을 사용해 비동기적으로 API 응답을 기다림

    response = await claude_client.messages.create(
        model= model, 
        messages= [{"role": "user", "content": prompt}], 
        max_tokens= 100
    )
    return response.content[0].text


async def main() :
    print("동시에 API 호출하기")
    prompt = "비동기 프로그래밍에 대해 두세 문장으로 설명해주세요."
    
    #비동기 함수 호출 시 코루틴 객체 반환 (실행 아직)
    openai_task = call_async_openai(prompt)
    claude_task = call_async_claude(prompt)

    #두 API 호출을 병렬로 실행하고 둘 다 완료될 때까지 대기
    openai_response, claude_response = await asyncio.gather(openai_task, claude_task)
    print(f"OpenAI 응답: {openai_response}")
    print(f"Claude 응답: {claude_response}")

if __name__ == "__main__": 
    asyncio.run(main()) #비동기 메인함수를 이벤트 루프에서 실행

### 비동기 함수를 실행하기 위한 함수명: asyncio.run()
### await main() 으로 쓰면 안되나? --> await은 함수 내에서만 사용 가능