import streamlit as st

#streamlit write 를 라이브러리에 쓰면 훌륭한 문서가 된다!! 그 외에도 다양한 자료형에서 사용할 수 있고, 잘 작동한다~

# st write를 안쓰고 자료형만 남겨놔도 페이지에서 보여준다..? 그래도 write를 쓰는게 코드 가독성을 높인다.




st.selectbox("너가 원하는 모델을 선택해봐", (
    "GPT-3",
    "GPT-3.5",
    "GPT-4",
))

st.markdown("""
    #### 이렇게~ 저렇게
""")
