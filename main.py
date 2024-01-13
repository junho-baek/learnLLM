from langchain.chat_models import ChatOpenAI
# from langchain.document_loaders import TextLoader
# loader = TextLoader('./files/chapter_one.txt')
# from langchain.document_loaders import PyPDFLoader
# loader = PyPDFLoader('./files/sample.pdf')
# 각각의 파일 로더가 아니라 구조화되어 있지 않은 파일을 불러오는 모듈
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter #일반적인 방법의 텍스트 분할 모듈
from langchain.text_splitter import CharacterTextSplitter #문자 단위로 분할하는 모듈

# splitter = RecursiveCharacterTextSplitter(
#   chunk_size = 200,
#   chunk_overlap = 50 #문장을 다 잘라먹을 경우에 앞 조각의 끝부분을 조금 가져와서 이어붙임.
# )

splitter = CharacterTextSplitter(
  separator="\n",
  chunk_size = 600,
  chunk_overlap = 100,
  # length_function = len
)

# loader = UnstructuredFileLoader('./files/sample.pdf')

loader = UnstructuredFileLoader('./files/demo.docx')


documents = loader.load_and_split(text_splitter=splitter)



print(documents[0].page_content)