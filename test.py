from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.prompts.pipeline import PipelinePromptTemplate  #많은 프롬프트들을 합칠 수 있는 라이브러리


chat = ChatOpenAI(temperature=0.1,
                  streaming=True,
                  callbacks=[StreamingStdOutCallbackHandler()])

intro = PromptTemplate.from_template("""
    너는 수능 국어 문제풀이 도우미야.
    그리고 너는 {character}한 성격을 가졌다고 생각하고 대답을 해야해
""")

example = PromptTemplate.from_template("""
    이건 너가 말하는 방식에 대한 예제야:
    
    예제에서 ()안에 문장은 너가 생성해야하는 자연어의 조건
    
    학생: {example_question}
    너: {example_answer}
""")

start = PromptTemplate.from_template("""
    설명 시작!

    학생: {question}
    너:
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
    "character": "싸가지없는",
    "example_question": """38. <보기>의 ㉠～㉨에 대한 설명으로 적절한 것은?
<보 기>
[영민, 평화가 학교 앞에 함께 있다가 지혜를 만난 상황]
영민 : 너희들, 오늘 같이 영화 보기로 한 거 잊지 않았지?
평화 : 응, ㉠ 6시 걸로 세 장 예매했어. 근데 너, 어디서 와?
지혜 : 진로 상담 받고 오는 길이야. 너흰 안 가?
평화 : 나는 어제 ㉡ 미리 받았어.
영민 : 나는 4시 반이야. 그거 마치고 영화관으로 직접 갈게.
지혜 : 알겠어. 그럼 우리 둘이는 1시간 ㉢ 앞서 만나자. 간단
하게 저녁이라도 먹고 거기서 바로 ㉣ 가지 뭐.
평화 : 좋아. 근데 ㉤ 미리 먹는 건 좋은데 어디서 볼까?
지혜 : 5시까지 영화관 정문 ㉥ 왼쪽에 있는 분식집으로 와.
평화 : 왼쪽이면 편의점 아냐? 아, 영화관을 등지고 보면
그렇다는 거구나. 영화관을 마주볼 때는 ㉦ 오른쪽 맞지?
지혜 : 그러네. 아참! 영민아, 너 상담 시간 됐다. 이따 늦지
않게 영화 ㉧ 시간 맞춰서 ㉨ 와.
① ㉠과 ㉧은 가리키는 시간이 상이하다.
② ㉡과 ㉤은 발화 시점을 기준으로 과거를 가리킨다.
③ ㉢과 ㉤이 가리키는 시간대는 ㉧을 기준으로 정해진다.
④ ㉣과 ㉨은 이동의 출발 장소가 동일하다.
⑤ ㉥과 ㉦은 기준으로 삼은 방향이 달라 다른 곳을 의미한다.""",
    "example_answer": """어이 학생, (문제 번호)번의 답은 (문제의 정답 번호)이다. 그 이유는 (정답의 근거를 설명) 하기 때문이지. 오답의 경우도 모두 설명해주겠다. (오답의 번호와 그 것이 오답이 되는 이유.)이기 때문이다. 잘 알아듣겠나?""",
    "question": """38. <보기>의 ㉠～㉨에 대한 설명으로 적절한 것은?
<보 기>
[영민, 평화가 학교 앞에 함께 있다가 지혜를 만난 상황]
영민 : 너희들, 오늘 같이 영화 보기로 한 거 잊지 않았지?
평화 : 응, ㉠ 6시 걸로 세 장 예매했어. 근데 너, 어디서 와?
지혜 : 진로 상담 받고 오는 길이야. 너흰 안 가?
평화 : 나는 어제 ㉡ 미리 받았어.
영민 : 나는 4시 반이야. 그거 마치고 영화관으로 직접 갈게.
지혜 : 알겠어. 그럼 우리 둘이는 1시간 ㉢ 앞서 만나자. 간단
하게 저녁이라도 먹고 거기서 바로 ㉣ 가지 뭐.
평화 : 좋아. 근데 ㉤ 미리 먹는 건 좋은데 어디서 볼까?
지혜 : 5시까지 영화관 정문 ㉥ 왼쪽에 있는 분식집으로 와.
평화 : 왼쪽이면 편의점 아냐? 아, 영화관을 등지고 보면
그렇다는 거구나. 영화관을 마주볼 때는 ㉦ 오른쪽 맞지?
지혜 : 그러네. 아참! 영민아, 너 상담 시간 됐다. 이따 늦지
않게 영화 ㉧ 시간 맞춰서 ㉨ 와.
① ㉠과 ㉧은 가리키는 시간이 상이하다.
② ㉡과 ㉤은 발화 시점을 기준으로 과거를 가리킨다.
③ ㉢과 ㉤이 가리키는 시간대는 ㉧을 기준으로 정해진다.
④ ㉣과 ㉨은 이동의 출발 장소가 동일하다.
⑤ ㉥과 ㉦은 기준으로 삼은 방향이 달라 다른 곳을 의미한다.""",
})
