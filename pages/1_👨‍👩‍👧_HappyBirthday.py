import streamlit as st
from PIL import Image

image=Image.open('IMG_20170513_082907.jpg')
st.image(image,caption='wife')