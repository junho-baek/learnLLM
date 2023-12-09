from langchain.chat_models import ChatOpenAI



chat = ChatOpenAI(
  temperature=0.1 #모델의 창의성, 높을 수록 창의적이다
)

from langchain.schema import HumanMessage, AIMessage, SystemMessage, messages

messages = [
  SystemMessage(content="You are a geography expert. And you only reply in korean"),
  AIMessage(content="안녕 내이름은 색마야"),
  HumanMessage(content="야 서울 부산 거리가 어떻게 돼? 그리고 너 이름이 뭐야?")
]

result= chat.predict_messages(messages)

print(result)


