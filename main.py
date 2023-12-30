from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

chat = ChatOpenAI(temperature=0.1)

from langchain.schema import BaseOutputParser

class CommaOutputParser(BaseOutputParser):
  def parse(self, text):
    items = text.strip().split(",")
    return list(map(str.strip, items)) #, 를 기준으로 텍스트를 나눠서 리스트로 만듬!

template = ChatPromptTemplate.from_messages(
  [
    ("system","You are a list generating machine. Everything you are asked will be answered with a comma separated list of max {max_items} in lowercase.Do NOT reply with anything else."),
    ("human", "{question}")
  ]
)

# prompt = template.format_messages(
#   max_items=10,
#   question="외우면 좋은 수준 높은 회화 영어 단어?"
# )
# result = chat.predict_messages(prompt)



# p = CommaOutputParser()

# print(p.parse(result.content))

chain = template | chat | CommaOutputParser()

result = chain.invoke({
  "max_items": 10,
  "question": "What are the top 10 most popular programming languages?"
})
print(result)