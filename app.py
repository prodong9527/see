import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

<<<<<<< HEAD
# Initialize the ChatOpenAI object
chat = None

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""
elif st.session_state["OPENAI_API_KEY"] != "":
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""

st.set_page_config(page_title="Welcome to ASL", layout="wide")

st.title("🤠 Welcome to ASL")

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
        prompt = st.chat_input("Type something...")
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
        st.warning("Please set your OpenAI API key in the settings page.")
=======
muti='''
今天是10.28，今明两天我将尝试完成这个应用的版面结构设计，开始生成和展示数据
'''
st.markdown(muti)

add_radio=st.sidebar.radio(
    "select",("one","two","three")
)

# df=pd.DataFrame(np.random.randn(50,20),columns=("第%d列" % i for i in range(20)))
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0))
>>>>>>> 95ffa71852e7f57b72485714112c438396ab6237
