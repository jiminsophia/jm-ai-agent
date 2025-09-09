### PromptTemplate 이란: 프롬프트를 객체로 관리하도록 하는 것
### --> 1. 재사용 및 유지보수 용이 
###     2. 동적 입력 처리 가능
###     3. Runnable 객체라서 LCEL 사용 가능

### PromptTemplate 생성방법 4가지
# 1. from_template() 활용: 문자열로 바로 생성
from langchain.prompts import PromptTemplate
template= PromptTemplate.from_template(
    "당신은 친절한 AI입니다. \n질문: {question}\n답변: "
)
print(template.format(question= "랭체인이 뭐죠?"))

print("=============================================")
# 2. 생성자 호출 --> 변수 목록, 템플릿 명시하여 세밀한 제어 가능
from langchain.prompts import PromptTemplate
template= PromptTemplate(
    input_variables= ['article', 'style'], 
    template= '다음 기사를 {style} 스타일로 요약하세요: \n\n{article}'
)
print(template.format(article= "OpenAI가 GPT-5를 공개했다...", style= '뉴스'))

print("=============================================")
# 3. load_prompt() 활용: 파일에서 템플릿 불러올 수 있음
import os
from langchain.prompts import load_prompt
current_dir_path= os.path.dirname(os.path.abspath(__file__))
file_prompt= load_prompt(f"{current_dir_path}/template_example.yaml")
print(file_prompt.format(context= "서울은 한국 수도이다.", question= "수도는?"))

print("=============================================")
# 4. partial_variables: 일부 변수를 고정하여 하위-프롬프트 생성 가능
from langchain.prompts import PromptTemplate
base_prompt= PromptTemplate.from_template("'{text}' 문장을 {lang}로 번역하세요.")
ko_prompt= base_prompt.partial(lang= "Korean")
en_prompt= base_prompt.partial(lang= "English")

print(ko_prompt.format(text= "Hello"))
print(en_prompt.format(text= "안녕하세요"))