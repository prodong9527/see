import streamlit as st
from PIL import Image

image=Image.open('images/IMG_20170513_082907.jpg')
st.image(image,caption='wife')