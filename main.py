
# 메모리에n설정한 메세지의 수 넘어가면 요약해서 저장
# 최근 대화에 더 중점을 두고 있는 요약 모델
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.1)


memory = ConversationSummaryBufferMemory(
  llm=llm,
  max_token_limit = 150,
  return_messages=True
)

def add_message(input, output):
  memory.save_context({"input": input}, {"output": output})

def get_history():
  return memory.load_memory_variables({})


add_message(input="안녕 나는 준호고 남한에 살고 있어", output="와 그거 멋진데?")


add_message(input="남한은 매우 멋져", output="나도 갈 수 있으면 좋겠다..")

print(get_history())