import streamlit as st
import os
from PIL import Image
import time

    # 设置图片文件夹路径
image_folder = 'images'

# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

# 设置图片尺寸
image_size = (300, 300)

# 初始化图片索引
image_index = 0

# 设置走马灯间隔时间（秒）
interval = 5

# 循环播放图片
while True:
    # 读取并调整图片尺寸
    image = Image.open(os.path.join(image_folder, image_files[image_index]))
    image = image.resize(image_size)
    
    # 显示图片
    st.image(image)
    
    # 更新图片索引
    image_index = (image_index + 1) % len(image_files)
    
    # 等待指定的时间间隔
    st.time.sleep(interval)