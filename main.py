from langchain.chat_models import ChatOpenAI



chat = ChatOpenAI(temperature=0.1)


b = chat.predict("안녕?")


print(b)