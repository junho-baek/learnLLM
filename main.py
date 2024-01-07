from langchain.memory import ConversationSummaryBufferMemory 

from langchain.chat_models import ChatOpenAI

from langchain.chains import LLMChain

from langchain.prompts import PromptTemplate

llm = ChatOpenAI (temperature=0.1)
memory = ConversationSummaryBufferMemory(
  llm=llm,
  max_token_limit=120,
  memory_key="chat_history",
)

template = """
    You are a helpful AI talking to a human.

    {chat_history}
    Human:{question}
    You:
"""
chain = LLMChain(
  llm=llm,
  memory=memory,
  prompt= PromptTemplate.from_template(template),
  verbose=True #프롬프트 로그들을 확인할 수 있는 프로퍼티
)
print(chain.predict(question="What is the capital of France?"))

print(chain.predict(question="I live in Seoul"))

print(memory.load_memory_variables({}))