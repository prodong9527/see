import streamlit as st
from PIL import Image


image=Image.open('IMG_20150707_211203_D1D.jpg')
st.image(image,caption='wife')