from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

chat_model= ChatOpenAI(model= "gpt-4.1-nano")

### BaseMessage 를 상속받은 클래스를 사용
# SystemMessage: 시스템 역할 지정, 페르소나 지정에 사용
# HumanMessage: 사용자의 입력이나 질문
# AIMessage: 채팅 모델의 응답에 사용
# ToolMessage: 도구 호출의 결과를 AI에 전달할 때 사용
# 이외에도 이름 뒤에 Chunk가 있다면? 스트리밍에서 사용한다는 의미임

messages= [
    SystemMessage(
        content="당신은 사용자의 질문에 간결하고 명확하게 답변하는 AI도우미 입니다."
    ),
    HumanMessage(content="LangChain에 대해 설명해주세요."),
    AIMessage(
        content="LangChain은 대규모 언어 모델(LLM)을 활용하여 애플리케이션을 구축하기 위한 프레임워크입니다."
    ),  # 이전 대화 예시
    HumanMessage(content="주요 기능 세 가지만 알려주세요."),  # 사용자의 질문
]

result= chat_model.invoke(messages) # 메시지의 리스트를 인자로 넘김
print("AI의 응답: ", result.content) #응답은 AIMessage 타입