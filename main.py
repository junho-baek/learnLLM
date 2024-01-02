from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

chat = ChatOpenAI(
    temperature=0.1,
)


with get_openai_callback() as usage:
    a = chat.predict("What is the recipe for soju")
    b = chat.predict("What is the recipe for bread")
    print(a, "\n")
    print(b, "\n")
    print(usage)


#사용량에 대해서 알 수 있다.

from langchain.chat_models import ChatOpenAI
from langchain.llms.openai import OpenAI

chat = OpenAI(
  temperature = 0.1,
  max_tokens = 450,
  model = "gpt-3.5-turbo-16k"
)

chat.save("model.json") # chat 설정을 저장.


from langchain.llms.loading import load_llm

chat = load_llm("model.json") # 모델을 불러올 수도 있다.