from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
# 벡터단위로 임베딩하는 모듈
from langchain.embeddings import OpenAIEmbeddings, CacheBackedEmbeddings
#벡터를 저장하는 공간
from langchain.vectorstores import Chroma
from langchain.storage import LocalFileStore

cache_dir = LocalFileStore("./cache/")


# embedder = OpenAIEmbeddings()

# 단어 하나
# vector = embedder.embed_query("Hi")
# print(vector)

# rank = len(vector)

# print(rank)

# 단어 여러개
# words = ["Hi", "Hello", "Bye", "Goodbye", "Thank you", "Thanks", "You're welcome", "Yes", "No", "Sorry"]
# vectors = embedder.embed_documents(words)

# print(vectors)

splitter = CharacterTextSplitter.from_tiktoken_encoder(
  separator="\n",
  chunk_size=600,
  chunk_overlap=100
)
loader = UnstructuredFileLoader("./files/chapter_one.txt")
docs = loader.load_and_split(text_splitter=splitter)

embeddings = OpenAIEmbeddings()

cached_embeddings = CacheBackedEmbeddings.from_bytes_store(
  embeddings,
  cache_dir
)


vectorstore = Chroma.from_documents(documents=docs, embedding=cached_embeddings)


result = vectorstore.similarity_search("Where does winston live")