#대화의 특정부분만 저장하는 모듈
from langchain.memory import ConversationBufferWindowMemory

#k 는 몇 개의 데이터를 저장할 지 설정하는 파라미터
memory = ConversationBufferWindowMemory(return_messages=True, k=4)


def add_message(input, output):
  memory.save_context({"input": input}, {"output": output})


add_message(0, 0)
add_message(1, 0)
add_message(2, 0)
add_message(3, 0)
add_message(4, 0)
# 최근 대화 메모리만 저장되어서 대화의 전반부 내용을 저장하기 어려울 수 있다.
print(memory.load_memory_variables({}))
