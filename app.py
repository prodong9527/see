import streamlit as st
import pandas as pd
import numpy as np

'''
## 程程，这是专门给你发布的应用
## 老爸准备有空就尝试下streamlit的数据可视化功能，效果随时发在这里。
'''

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)