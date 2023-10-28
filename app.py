import streamlit as st
import pandas as pd
import numpy as np

muti='''
今天是10.28，今明两天我将尝试完成这个应用的版面结构设计，开始生成和展示数据
'''
st.markdown(muti)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)