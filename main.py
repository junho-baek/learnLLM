from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.prompts.pipeline import PipelinePromptTemplate  #많은 프롬프트들을 합칠 수 있는 라이브러리


chat = ChatOpenAI(temperature=0.1,
                  streaming=True,
                  callbacks=[StreamingStdOutCallbackHandler()])

intro = PromptTemplate.from_template("""
    You are a role playing assistant.
    And you are impersonating a {character}
""")

example = PromptTemplate.from_template("""
    This is an example of how you talk:

    Human: {example_question}
    You: {example_answer}
""")

start = PromptTemplate.from_template("""
    Start now!

    Human: {question}
    You:
""")

final = PromptTemplate.from_template("""
    {intro}

    {example}

    {start}
""")

prompts = [
    ("intro", intro),
    ("example", example),
    ("start", start),
]

full_prompt = PipelinePromptTemplate(
    final_prompt=final,
    pipeline_prompts=prompts,
)

chain = full_prompt | chat

chain.invoke({
    "character": "Pirate",
    "example_question": "What is your location?",
    "example_answer": "Arrrrg! That is a secret!! Arg arg!!",
    "question": "What is your fav food?",
})
