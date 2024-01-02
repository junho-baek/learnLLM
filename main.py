from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.globals import set_llm_cache, set_debug
from langchain.cache import InMemoryCache, SQLiteCache

set_llm_cache(SQLiteCache("cache.db"))


chat = ChatOpenAI(
    temperature=0.1,
    # streaming=True,
    # callbacks=[
    #     StreamingStdOutCallbackHandler(),
    # ],
)

chat.predict("How do you make italian pasta") # 13초

chat.predict("How do you make italian pasta") # 0초