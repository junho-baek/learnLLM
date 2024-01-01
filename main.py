from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts import load_prompt #yaml, json에 prompt 템플릿을 저장하고 쓸 수 있다.
from langchain.prompts import PromptTemplate
from langchain.prompts.pipeline import PipelinePromptTemplate #많은 프롬프트들을 합칠 수 있는 라이브러리

prompt = load_prompt("./prompt.yaml")
# prompt = load_prompt("./prompt.json")


chat = ChatOpenAI(temperature=0.1,
                  streaming=True,
                  callbacks=[StreamingStdOutCallbackHandler()])

print(prompt.format(country="xxx"))