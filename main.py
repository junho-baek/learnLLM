from langchain.memory import ConversationSummaryBufferMemory 

from langchain.chat_models import ChatOpenAI

from langchain.chains import LLMChain

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI (temperature=0.1)
memory = ConversationSummaryBufferMemory(
  llm=llm,
  max_token_limit=120,
  memory_key="chat_history",
  return_messages=True,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI talking to a human"),
        MessagesPlaceholder(variable_name="chat_history"),#채팅 기록을 남긴다.
        ("human", "{question}"),
    ]
)
chain = LLMChain(
  llm=llm,
  memory=memory,
  prompt= prompt,
  verbose=True #프롬프트 로그들을 확인할 수 있는 프로퍼티
)
print(chain.predict(question="What is the capital of France?"))

print(chain.predict(question="I live in Seoul"))

print(memory.load_memory_variables({}))