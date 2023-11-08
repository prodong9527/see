import streamlit as st

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""

st.set_page_config(page_title="OpenAI Settings", layout="wide")

"""
### OpenAI APIKey Settings
"""

# openai_api_key = st.text_input("API Key", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None, type='password')

saved = st.button("💝💝💝")

if saved:
    st.session_state["OPENAI_API_KEY"] = "sk-qz"+"XatBZbVs6LEYszh"+"4bzT3BlbkFJimY"+"3n060Mphi9loktDXM"