from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

### RunnablePassthrough: 데이터 흐름 제어할 때 유용하게 쓰임

prompt= ChatPromptTemplate.from_template(
    "주어진 '{word}와 유사한 단어 3가지를 나열해주세요. 단어만 나열합니다."
)
model= ChatOpenAI(model= 'gpt-4.1-nano')
parser= StrOutputParser()

# 병력 처리 체인 구성
chain= RunnableParallel(
    {
        'original' : RunnablePassthrough(),     # 원본 데이터 보존
        'processed': prompt | model | parser,   # 처리된 데이터
    }
)

result= chain.invoke({'word' : '행복'})
print(result)   # {'original': {'word': '행복'}, 'processed': '기쁨, 환희, 만족'} <-- 이렇게 리턴
