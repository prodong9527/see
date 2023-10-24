import streamlit as st
from sklearn import datasets

iris = datasets.load_iris()
st.title('This is a title')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')
st.markdown('# This is markdown')
