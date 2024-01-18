from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, CacheBackedEmbeddings
from langchain.vectorstores import FAISS
from langchain.storage import LocalFileStore


# 이건 Retrieval을 쉽게 할 수 있는 모듈인데, 다음시간에 프롬프트 엔지니어링을 통해서 이를 직접 구현할 것임.
from langchain.chains import RetrievalQA

llm = ChatOpenAI()

cache_dir = LocalFileStore("./cache/")

splitter = CharacterTextSplitter.from_tiktoken_encoder(
    separator="\n",
    chunk_size=600,
    chunk_overlap=100,
)
loader = UnstructuredFileLoader("./files/chapter_one.txt")

docs = loader.load_and_split(text_splitter=splitter)

embeddings = OpenAIEmbeddings()

cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)

vectorstore = FAISS.from_documents(docs, cached_embeddings)

chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="map_reduce", #stuff 가 디폴트값이다. refine, map_reduce, map_rerank, map_reduce_refine 등의 옵션이 있다. 이것이 궁금하면 공식 문서로!
    retriever=vectorstore.as_retriever(), # retriever를 이용하면 vectorstore에서뿐만 아니라 데이터베이스와 같은 저장소에서도 document를 불러와 답변에 사용할 수 있다.
)

print(chain.run("Describe Victory Mansions"))


# load, split, embed(vector), cahce vector, vectorstore, chain(retrivalQA) 등을 배움