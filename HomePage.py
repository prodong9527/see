import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Initialize the ChatOpenAI object
chat = None

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""
elif st.session_state["OPENAI_API_KEY"] != "":
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])

st.set_page_config(page_title="🐠 夜风习习", layout="wide")

st.title("🤠 小团团都想死你了")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if chat:
    with st.container():
        for message in st.session_state["messages"]:
            if isinstance(message, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant"):
                    st.markdown(message.content)
        prompt = st.chat_input("萍萍主人有什么问题...")
        if prompt:
            st.session_state["messages"].append(HumanMessage(content=prompt))
            with st.chat_message("user"):
                st.markdown(prompt)
            ai_message = chat([HumanMessage(content=prompt)])
            st.session_state["messages"].append(ai_message)
            with st.chat_message("assistant"):
                st.markdown(ai_message.content)
else:
    with st.container():
        st.warning("萍萍主人，请到[APIkey页面]点💝💝💝再回来")

with st.sidebar:
    click = st.checkbox('萍萍click')
    if click:
        st.markdown('''
### :orange[亲爱的老婆]
### :orange[祝你永远十八岁!]
### :orange[不管几岁，快乐万岁！]
''')