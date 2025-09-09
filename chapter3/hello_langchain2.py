from langchain.chat_models import init_chat_model

model= init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic") # 모델 초기화
result= model.invoke("랭체인이 뭔지 한줄로 설명해주세요") # 모델 실행
print(result.content) # 결과값
