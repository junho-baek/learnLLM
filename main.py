from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough #메모리를 불러오는걸 자동으로 해주는 모듈
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(temperature=0.1)

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=120,
    return_messages=True,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI talking to a human"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)


def load_memory(_):
    return memory.load_memory_variables({})["history"]#저장된 내용을 불러오기

# 첫 체인이 작동할 때 1개의 파라미터가 있어야해서 그런 함수를 설정
chain = RunnablePassthrough.assign(history=load_memory) | prompt | llm


def invoke_chain(question):
    result = chain.invoke({"question": question})
    memory.save_context(
        {"input": question},
        {"output": result.content},
    )#메모리에 저장
    print(result)

invoke_chain("My name is nico")
invoke_chain("What is my name?")