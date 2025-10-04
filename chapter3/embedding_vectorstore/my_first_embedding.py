from langchain_openai import OpenAIEmbeddings
import numpy as np

# 임베딩 모델 초기화
# OpenAI의 ext-embedding-3-large 모델 호출하여 사용: 60억 토큰 학습, 3072차원 벡터 반환하는 모델-> 다국어 의미 파악 성능 높음
embeddings= OpenAIEmbeddings(model= 'text-embedding-3-large')

# 단어들을 임베딩으로 변환
words= ["강아지", "고양이", "자동차", "비행기"]
word_embeddings= embeddings.embed_documents(words)

# 쿼리 임베딩 생성: 쿼리와 문서 임베딩 차원이 같아야 코사인 유사도 비교 가능
query= "동물"
query_embedding= embeddings.embed_query(query)

# 코사인 유사도 계산 함수
def cosine_similarity(vec1, vec2): 
    """두 벡터 간의 코사인 유사도를 계산합니다."""
    dot_product= np.dot(vec1, vec2)
    norm_vec1= np.linalg.norm(vec1)
    norm_vec2= np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2 + 1e-9) #   작은 값 추가로 0나누기 방지

# 각 단어와 쿼리의 유사도 계산
print(f" '{query}'에 대한 유사도: ")
for word, embedding in zip(words, word_embeddings): 
    similarity= cosine_similarity(query_embedding, embedding)
    print(f"    {word}: {similarity:.3f}")
