from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate

chat = ChatOpenAI(temperature=0.1)

# template = PromptTemplate.from_template("What is the distance between {country_a} and {country_b}?")

# prompt = template.format(country_a="South Korea", country_b="Japan")

# print(chat.predict(prompt))


template = ChatPromptTemplate.from_messages(
  [
  ("system", "You are a geography expert. And you only reply in {language}"),
  ("ai", "Hi, my name is {name}"),
  ("human", "What is the distance between {country_a} and {country_b}?. Also, what is your name?")

  ]
)

prompt = template.format_messages(
  language="korean",
  name="탱이",
  country_a="South Korea",
  country_b="Japan"
)

print(chat.predict_messages(prompt))


