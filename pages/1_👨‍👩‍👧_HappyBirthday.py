import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="幸福记忆", layout="wide")

st.header('这里有永远留在我们记忆中的:blue[幸福]:sunglasses:', divider='rainbow')
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
    
    # 显示图片
    st.image(image,width=380,caption=image_index.split(".")[0])

