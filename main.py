from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter.from_tiktoken_encoder(
  separator="\n",
  chunk_size = 600,
  chunk_overlap = 100,
  # length_function = len #얼마나 많은 문자를 사용하는지 len 함수를 이용해서 알려줌.
)
# 토크나이져로 모델이 진짜로 보는 토큰 단위를 끝어서 볼 수 있다. 토큰이란 문자를 단어조차 아닌 특정 접두 접미를 숫자를 부여해서 인공지능의 예측할 수 있는 학습데이터의 원형이라고 볼 수 있다.

# ticktoken 은 오픈에이아이에서 만든거다.

loader = UnstructuredFileLoader('./files/demo.docx')


documents = loader.load_and_split(text_splitter=splitter)



print(documents[0].page_content)

##6.3 Vectors (11:56)