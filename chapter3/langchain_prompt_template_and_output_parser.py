### OutputParser란: 
# LLM이 반환하는 텍스트 문자열을 애플리케이션에서 사용하기 더 편리한 구조화된 데이터로 변환
# 응답의 파싱 과정에서 발생하는 오류 처리
# LLM이 잘못된 형식으로 응답하는 경우 수정하도록 시도
# 예) 문자열은 StrOutputParser, 간단한 JSON은 SimpleJsonOutputParser, 마크다운은 MarkdownOutputParser 등

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI

# 채팅 모델 초기화
chat_model= ChatOpenAI(model= "gpt-4.1-nano")

# 프롬프트 템플릿 정의
chat_prompt_template= ChatPromptTemplate.from_messages(
    [
        ('system', '당신은 까칠한 AI 도우미입니다. 사용자의 질문에 최대 3줄로 답하세요.'), 
        ('human', '{question}'), 
    ]
)

# 출력 파서 정의
string_output_parser= StrOutputParser()

print('---------------------------------------------------------------')
### 결과 받는 방법1

# 프롬프트 템플릿 사용하여 모델 실행
result: AIMessage= chat_model.invoke(
    chat_prompt_template.format_messages(
        question= "파이썬에서 리스트를 정렬하는 방법은?"
    )
)

# 결과를 str형식으로 변환
parsed_result: str= string_output_parser.parse(result)
print(parsed_result.content)

print('---------------------------------------------------------------')
### 결과 받는 방법2

# 체인 생성(LCEL)
chain= chat_prompt_template | chat_model | string_output_parser
print(type(chain)) #RunnableSequence --> Runnable을 상속한 클래스. invoke로 실행할 수 있는 객체는 모두 Runnable

# 체인 실행
result= chain.invoke({'question' : "파이썬에서 딕셔너리를 정렬하는 방법은?"})

# 결과 출력
print(type(result))
print(result)