### Runnable 이란: '실행 가능한 무언가'를 나타내는 추상 인터페이스 --> 입력을 받아서 출력을 생성하는 모든 것
### 1. 통일된 인터페이스 : 모든 runnable은 같은 메서드 제공--> 어떤 컴포넌트든 예측 가능한 방식으로 사용 가능
### 2. 조합 가능성: 파이프 연산자로 쉽게 연결 가능 (|)
### 3. 다양한 실행 모드: 동기/비동기/스트리밍/배치 처리 전부 지원
### 4. 타입 안정성: 입/출력 타입 명시 가능 --> 타입 체커 도움 받기 가능

from langchain_core.runnables import RunnableLambda

# 일반 함수를 runnable로 변환
def add_exclamation(text: str) -> str: 
    """텍스트 끝에 느낌표 추가하는 함수"""
    return f"{text}!"

# RunnableLambda로 감싸서 Runnable로 만들기
exclamation_runnable= RunnableLambda(add_exclamation)

# 다양한 방식으로 실행 가능 --> invoke는 단일 입력 처리
result= exclamation_runnable.invoke("안녕하세요")
print(result)

# 배치 처리도 자동 지원 --> batch로 여러 입력 처리, 리스트로 입/출력
results= exclamation_runnable.batch(["안녕", "반가워", "좋은 아침"])
print(results)