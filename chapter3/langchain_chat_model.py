import random
from langchain.chat_models import init_chat_model

if random.random() < 0.5: # 50% 확률로 gpt-4.1-nano 선택
    print("gpt-4.1-nano selected")
    model= init_chat_model("gpt-4.1-nano", model_provider= "openai")
else: 
    print("claude-sonnet-4-20250514 selected")
    model= init_chat_model("claude-sonnet-4-20250514", model_provider= "anthropic")

result= model.invoke("RAG가 뭔지 한줄로 설명해주세요")
print(result.content)