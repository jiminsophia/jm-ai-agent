from agents import Agent, Runner

#에이전트 생성
hello_agent= Agent(
    model= 'gpt-4.1-nano', 
    name='HelloAgent', 
    instructions= "당신은 HelloAgent 입니다. 당신의 임무는 '안녕하세요' 라고 인사하는 겁니다."
)

#에이전트 실행
#기본 함수인 run()은 비동기 함수임 --> 에이전트에게 요청하는 작업은 오래 걸리는 경우가 많기 때문
result= Runner.run_sync(hello_agent, "프랑스어로만 인사해주세요.")

#결과 출력
print(result.final_output)