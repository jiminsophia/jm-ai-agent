from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter

#임베딩 모델과 텍스트 분할기 준비
#문서 특성에 따라 separator 잘 써야함
#chunk size=50 은 문서 하나에 문자 50개가 들어간다는 의미로, 칼같이 끊지는 않고 되도록 separator 기준으로 나눠서 들어감
#chunk_overlap= 20 은 문서를 쪼갤 때 20개의 문자 정도의 구간은 겹치게 하여, 쪼개진 문서의 앞뒤 문맥 알 수 있게.
embeddings= OpenAIEmbeddings()
text_splitter= CharacterTextSplitter(separator=".", chunk_size= 50, chunk_overlap= 20)

#샘플 문서들 준비
#단순 텍스트가 아닌 document 객체를 사용하며, page_content에 내용을 담고 metadata에는 해당 문서에 대한 추가 정보 담음
documents= [
    Document(
        page_content="파이썬은 읽기 쉽고 배우기 쉬운 프로그래밍 언어입니다. "
        "다양한 분야에서 활용되며, 특히 데이터 과학과 AI 개발에 인기가 높습니다.",
        metadata={"source": "python_intro.txt", "topic": "programming"},
    ),
    Document(
        page_content="자바스크립트는 웹 브라우저에서 실행되는 프로그래밍 언어로 시작했지만, "
        "현재는 서버 사이드 개발에도 널리 사용됩니다. Node.js가 대표적입니다.",
        metadata={"source": "js_guide.txt", "topic": "programming"},
    ),
    Document(
        page_content="머신러닝은 데이터에서 패턴을 학습하는 AI의 한 분야입니다. "
        "지도학습, 비지도학습, 강화학습 등 다양한 방법론이 있습니다.",
        metadata={"source": "ml_basics.txt", "topic": "ai"},
    ),
]

#분서 분할
split_docs= text_splitter.split_documents(documents)
for doc in split_docs: 
    print(f"문서: {doc.page_content[:50]}... | 출처: {doc.metadata['source']} | 주제: {doc.metadata['topic']}")

#FAISS 벡터스토어 생성
vectorstore= FAISS.from_documents(split_docs, embeddings)

#유사도 검색 수행
#similarity_search는 질문도 같은 임베딩 모델을 통해 벡터로 변환하고, 질문 벡터와 저장된 모든 문서 벡터 간의 거리 계산
query= "초보자가 배우기 좋은 프로그래밍 언어는?"
results= vectorstore.similarity_search(query, k= 2)

print(f"질문: {query}\n")
print("검색 결과: ")
for i, doc in enumerate(results, 1): 
    print(f"\n{i}.{doc.page_content[:100]}...")
    print(f"    출처: {doc.metadata['source']}")
    print(f"    주제: {doc.metadata['topic']}")

#유사도 점수와 함께 검색
#FAISS 유사도는 코사인 유사도와 반대로 점수가 낮을수록 더 유사함을 의미
results_with_scores= vectorstore.similarity_search_with_score(query, k= 2)
print("\n\n유사도 점수: ")
for doc, score in results_with_scores: 
    print(f"- {doc.metadata['source']}: {score:.3f}")


#임베딩을 잘 사용하려면 문자열을 소스 코드에 넣는 것이 아니라, 다른 곳에서 불러와서 사용해야 함 --> vectorestore_with_document_loader.py
#FAISS 벡터DB의 장점: 연구/ 프로토타입/ 작은 규모의 애플리케이션에서 좋음
#             한계점: 확장성/ 분산 처리 어려움/ 실시간 업데이트 안됨/ 운영 및 관리 어려움 등
#기타 벡터DB로는 Chroma. Pinecone, Weaviate, pgvector, Elasticsearch, Qdrant 등이 있음