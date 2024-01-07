# knowledge graph
# 중요도에 따라 요약해준다
from langchain.memory import ConversationKGMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.1)


memory = ConversationKGMemory(
  llm=llm,
  return_messages=True
)

def add_message(input, output):
  memory.save_context({"input": input}, {"output": output})



# 저장
add_message("say hi to sam", "who is sam")
add_message("sam is a friend", "okay")

# 출력
print(memory.load_memory_variables({"input": "who is sam"}))