
# 대화 내용을 자체적으로 요약해서 저장해주는 모델
# 대화 내용이 짧으면 더 많은 토큰을 소비할 수 있겠지만, 길면 길수록 효율적으로 저장할 수 있는 모델

from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.1)


memory = ConversationSummaryMemory(llm=llm)

def add_message(input, output):
  memory.save_context({"input": input}, {"output": output})

def get_history():
  return memory.load_memory_variables({})


add_message(input="안녕 나는 준호고 남한에 살고 있어", output="와 그거 멋진데?")


add_message(input="남한은 매우 멋져", output="나도 갈 수 있으면 좋겠다..")

print(get_history())