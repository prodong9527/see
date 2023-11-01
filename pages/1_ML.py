import streamlit as st
import os
from PIL import Image

image_files = [f for f in os.listdir('/images') if f.endswith(('.jpg', '.jpeg', '.png'))]

# 设置每张图片显示的时间（秒）
display_time = 5

# 循环显示图片
for image_file in image_files:
    # 读取图片
    image = Image.open(image_file)
    
    # 显示图片
    st.image(image, caption=image_file)
    
    # 等待指定的时间
    st.write(f"<br>", unsafe_allow_html=True)
    st.stop()