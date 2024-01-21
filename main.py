from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, CacheBackedEmbeddings
from langchain.vectorstores import FAISS
from langchain.storage import LocalFileStore
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
llm = ChatOpenAI(
    temperature=0.1,
)

# map reduce LCEL chain 만들기 위한 구상~
# list of docs
# for doc in list of docs | prompt | llm

# for response in list of llms response | put them all together

# final doc | prompt | llm

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

retriever = vectorstore.as_retriever()

#---------------


QUESTION = "Describe Victory Mansions"

map_doc_prompt = ChatPromptTemplate.from_messages(
  [
    (
      "system",
      "Use the following context of a long document to see if any of the text is relevant to answer the question. Return any relevant text verbatim.\n ------ \n {context}"
    ),
    (
      "human",
      "question"
    ),
  ]
)

map_doc_chain = map_doc_prompt | llm




def map_docs(inputs):
  
  documents = inputs["documents"]
  question = inputs["question"]
  # results = []
  # for document in documents:
  #   result = map_doc_chain.invoke(
  #     {
  #       "context": document.page_content,
  #       "question": question,
  #     }
  #   ).content
  #   results.append(result)
  #   results = "\n\n".join(results)
  
  return "\n\n".join(
      map_doc_chain.invoke(
          {"context": doc.page_content, "question": question}
      ).content
      for doc in documents
  )
  

#RunnableLambda는 체인에서 함수를 호출할 수 있게 해주는 모듈
map_chain = {
  "documents": retriever,
  "question": RunnablePassthrough()
} | RunnableLambda(map_docs)


#RunnablePassthrough chain 이 innvoke 될 때 파라미터를 그대로 가져옴

final_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Given the following extracted parts of a long document and a question, create a final answer.
            If you don't know the answer just say you don't know, don't try to make up an answer.
            ------
            {context}
            """,
        ),
        ("human", "{question}"),
    ]
)


chain = {"context": map_chain, "question": RunnablePassthrough()
        } | final_prompt | llm


print(chain.invoke(QUESTION))


