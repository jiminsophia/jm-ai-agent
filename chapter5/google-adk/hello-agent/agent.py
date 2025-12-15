from google.adk.agents import Agent

# 인사말 함수
def greet_user() -> str: 
    return "안녕하세요!"

# 루트 에이전트 선언
# ADK에서 루트 에이전트는 agent.py 의 형태로 반드시 있어야 함
# 실행 방법은 총 3가지: 1) adk web (web UI) 
#                   2) adk run (terminal) 
#                   3) adk api_server (FastAPI server)
# agent.py가 저장된 디렉토리의 상위 디렉토리로 이동한 뒤 터미널에서 실행 (이 경우 chapter5/google-adk 에서 실행)
root_agent= Agent(
    name= 'hello_agent', 
    model= 'gemini-2.5-flash', 
    description= "유저와 인사하는 에이전트입니다.", 
    instruction= "사용자에게 반갑고 친절하게 인사해주세요.", 
    tools= [greet_user]
)
