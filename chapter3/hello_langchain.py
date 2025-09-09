from langchain.chat_models import init_chat_model

model= init_chat_model("gpt-4.1-nano", model_provider="openai") # LLM 초기화
result= model.invoke("랭체인이 뭔지 한줄로 설명해주세요") # 모델 실행
print(type(result)) # AIMessage 타입
print(result.content) # 결과값
