
# 전통적인 방법의 모든 대화내용을 메모리화 하는 모듈
# 자동완성과 같은 일회성 기능에 유용하다.
# chat 모델에는 비용적으로 부적합하다.
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)
# return_messages=True 옵션을 넣어주면 메세지 형식으로 메모리를 불러온다. 챗봇을 위한 옵션, False인 경우에는 메모리를 스트링 형식으로 불러온다.


memory.save_context({"input": "Hi"}, {"output": "How are you?"})

print(memory.load_memory_variables({}))