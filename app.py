import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Initialize the ChatOpenAI object

chat = None
prompt_l="你叫'小团团'，现在你正在为'萍萍主人'服务，11月6日是她的生日，你在回答问题前请先介绍自己。//"
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = "sk-qmG"
elif st.session_state["OPENAI_API_KEY"] != "":
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])

st.set_page_config(page_title="🐠夜风习习", layout ="wide")

st.title("🤠")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if chat:
    with st.container():
        st.header("Chat with GPT")

        for message in st.session_state["messages"]:
            if isinstance(message, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant"):
                    st.markdown(message.content)
        prompt = st.chat_input("Can I help you...")
        if prompt:
            st.session_state["messages"].append(HumanMessage(content=prompt))
            
            with st.chat_message("user"):
                st.markdown(prompt)
            ai_message = chat([HumanMessage(content=prompt)])
            st.session_state["messages"].append(ai_message)
            with st.chat_message("assistant"):
                st.markdown(ai_message.content)
            st.session_state["messages"]
else:
    with st.container():
        st.warning("Please set your OpenAI API key in the settings page.")

