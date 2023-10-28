import streamlit as st
import pandas as pd
import numpy as np

muti='''
今天是10.28，今明两天我将尝试完成这个应用的版面结构设计，开始生成和展示数据
'''
st.markdown(muti)

st.sidebar.spinner("Loading...")
time.sleep(5)
st.success("Done!")

df=pd.DataFrame(np.random.randn(50,8),columns=("第d%列" % i for i in range(8)))
st.dataframe(df.style.highlight_max(axis=0))