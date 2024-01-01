from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.few_shot import FewShotChatMessagePromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler


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

example_prompt = ChatPromptTemplate.from_messages(
    [("human", "What do you know about {question}?"),
    ("ai", "{answer}")
    ])

example_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)
final_prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a geography expert, you give short answers."),
  example_prompt,
  ("human", "What do you know about {country}"),
])

chain = final_prompt | chat

chain.invoke(
  {
    "country": "태국"
  }
)