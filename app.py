import streamlit as st
import pandas as pd
import numpy as np

muti='''
今天是10.28，今明两天我将尝试完成这个应用的版面结构设计，开始生成和展示数据
'''
st.markdown(muti)

add_radio=st.sidebar.radio(
    "select",("one","two","three")
)

df=pd.DataFrame(np.random.randn(50,20),columns=("第%d列" % i for i in range(20)))
# df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0))