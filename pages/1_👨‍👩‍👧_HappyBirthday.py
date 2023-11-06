import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="天鱼精选", layout="wide")

image_folder='images'
# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
# 设置图片尺寸

# 初始化图片索引
image_index = 0

# 循环播放图片
for image_index in image_files:
    # 读取并调整图片尺寸
    image = Image.open(os.path.join(image_folder, image_index))
    image = image.width(600)
    
    # 显示图片
    st.image(image)

