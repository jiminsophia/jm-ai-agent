from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model

llm= init_chat_model("gpt-4.1-nano", model_provider="openai")

### pydantic: 타입 힌트를 사용해 데이터 검증과 설정 관리를 쉽게 하는 파이썬 라이브러리
# 랭체인에서는 데이터 스키마 정의에 자주 사용

class MovieReview(BaseModel): 
    """영화 리뷰 스키마 정의"""
    title: str= Field(description= "영화 제목")
    rating: float= Field(description= "10점 만점 평점 (예: 7.5)")
    review: str= Field(description= "한글 리뷰 (3~4 문장)")

# 모델에 스키마 바인딩
structured_llm= llm.with_structured_output(MovieReview)

# llm의 실행 결과가 MovieReview타입으로 넘어옴
result: MovieReview= structured_llm.invoke(
    "영화 '기생충'에 대 한 리뷰를 작성해주세요."
)

print(result.title)
print(result.rating)
print(result.review)