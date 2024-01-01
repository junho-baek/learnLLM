from langchain.chat_models import ChatOpenAI
from langchain.prompts import example_selector
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts.example_selector.base import BaseExampleSelector
from langchain.prompts.example_selector import LengthBasedExampleSelector  # 길이기반으로 예제들을 선택해준다.

chat = ChatOpenAI(temperature=0.1,
                  streaming=True,
                  callbacks=[StreamingStdOutCallbackHandler()])

examples = [
    {
        "question":
        "What do you know about France?",
        "answer":
        """
Here is what I know:
Capital: Paris
Language: French
Food: Wine and Cheese
Currency: Euro
""",
    },
    {
        "question":
        "What do you know about Italy?",
        "answer":
        """
I know this:
Capital: Rome
Language: Italian
Food: Pizza and Pasta
Currency: Euro
""",
    },
    {
        "question":
        "What do you know about Greece?",
        "answer":
        """
I know this:
Capital: Athens
Language: Greek
Food: Souvlaki and Feta Cheese
Currency: Euro
""",
    },
]
#exampleSelector는 아래와 같은 메서드를 가지고 있어야 합니다. add, select_examples
class RandomExampleSelector(BaseExampleSelector):
  def __init__(self, examples):
      self.examples = examples

  def add_example(self, example):
      self.examples.append(example)

  def select_examples(self, input_variables):
      from random import choice

      return [choice(self.examples)]


example_prompt = PromptTemplate.from_template("Human: {question}\nAI:{answer}")

example_selector = RandomExampleSelector(
    examples=examples,
)
# 개체가 생성될 때 이미 예제들을 넣어둠
print(example_selector)
prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    example_selector=example_selector, # 개체를 받는 파라미터
    suffix="Human: What do you know about {country}?",
    input_variables=["country"],
)


print(prompt.format(country="Brazil"))
