import random
from langchain.tools import tool
from langchain_openai import ChatOpenAI

### @tool 데코레이터 사용 시 주의점
### 1. 독스트링 작성 필수, 명확하고 구체적으로: AI는 이 설명을 읽고 도구를 선택하기 때문
###     ex) "계산을 수행합니다" -> "두 숫자의 사칙연산을 수행하며, 0으로 나누기 에러를 안전하게 처리합니다"
### 2. 세밀한 에러 처리: AI가 예상치 못한 입력 전달할 수 있음 -> 최대한 모든 에러 고려, 사용자 친화적 메시지 반환하도록


# 가위바위보 게임을 위한 tool 정의
# 데코레이터 사용하여 일반 함수 -> 랭체인 함수로 변환
@tool
def rps() -> str: 
    """가위바위보 중 하나를 랜덤하게 선택"""
    return random.choice(["가위", "바위", "보"])

# Tool 바인딩된 LLM
llm= ChatOpenAI(temperature=0.0).bind_tools([rps])  # rps() 함수와 LLM 연결 -> LLM이 rps() 함수 도구로 호출 가능
llm_for_chat= ChatOpenAI(temperature= 0.7)  # 해설용 LLM: llm에는 rps 도구를 사용하도록 유도해둔 상태이기 때문에 llm은 텍스트 생성이 아닌 rps 도구를 사용하려고 함 -> 텍스트 생성용 모델 따로 정의
print(type(llm))    # RunnableBinding: 도구가 바인딩된 Runnable

# 승부 판정
def judge(user_choice, computer_choice): 
    """가위바위보 승패를 판정합니다."""
    user_choice= user_choice.strip()
    computer_choice= computer_choice.strip()
    if user_choice == computer_choice: 
        return "무승부"
    elif (user_choice, computer_choice) in [
        ("가위", "보"), 
        ("보", "바위"), 
        ("바위", "가위"), 
    ]: 
        return "승리"
    else: 
        return "패배"
    
# 게임 루프
print("가위바위보! (종료: q)")
while (user_input := input("\n가위/바위/보: ")) != "q":     # 바다코끼리 연산자: 입력과 동시에 조건 검사 수행
    #LLM에게 tool 호출 요청: 어떤 도구 사용할지 선택. rps라는 도구를 사용하도록 명시하여 지시
    ai_msg= llm.invoke(
        f"가위바위보 게임: 사용자가 {user_input}를 냈습니다. rps tool을 사용하세요."
    )

    # Tool 호출 확인 및 실행
    if ai_msg.tool_calls:   # tool_calls: LLM이 호출하려는 도구들의 목록. 배열이 빈 값이 아니라면 tool 호출이 있다는 뜻. 
        print(type(rps))    # StructuredTool; runnable인터페이스를 구현하고 있어서 실행시 invoke 사용
        llm_choice= rps.invoke("")  # Tool 호출 실행. 인자 필요 없어서 빈 string이나 dict 넣어서 실행; 아예 안 넣으면 에러남
        print(f"    LLM이 선택한 도구: {llm_choice}")
        result= judge(user_input, llm_choice)

        print(f"승부: {result}")    # 기존 print(f"{result}") 보다 명확하게

        # 결과 응답 생성
        final= llm_for_chat.invoke(
            f"가위바위보 게임 결과를 재미있게 해설해주세요."
            f"사용자: {user_input}, AI: {llm_choice}, 결과: 사용자의 {result}"
        )
        print(final)
        print(f"    LLM 해설: {final.content}")
        print(f"게임 요약: 당신({user_input}) vs AI({llm_choice}) => {result}")
    else: 
        print("Tool 호출 실패")