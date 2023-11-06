import streamlit as st

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = "qmG51LjsHPWgwqdpg9A6T3BlbkFJZGpYExgOwGgXk23yrcL"

st.set_page_config(page_title="OpenAI Settings", layout="wide")

st.title("Settings")

openai_api_key = st.text_input("API Key", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None, type='password')

saved = st.button("Save")

if saved:
    st.session_state["OPENAI_API_KEY"] = openai_api_key