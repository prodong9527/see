import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="幸福记忆", layout="wide")

st.markdown("## 永远留在我们记忆里的幸福 &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:  " 
            )
st.markdown("----------")
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
    st.image(image,use_column_width=True)
    md=image_index.split(".")[0]
    
    st.markdown(f"""### 👪<span style="color:red">{md}</span>
""",unsafe_allow_html=True)
    st.divider()

st.caption("接下来请欣赏AI作品")
col1,col2 = st.columns(2)
with col1:
    st.image("1.jpg")
    st.image("2.jpg")
with col2:
    st.image("3.jpg")
    st.image("4.jpg")

st.write('知道不咋地，星火大模型尽力了😵‍💫')
