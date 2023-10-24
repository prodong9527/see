import streamlit as st
import pandas as pd
import numpy as np
'''
建立streamlit和本地vscode的自动连接

20231024测试success
'''
chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

st.area_chart(chart_data, x="col1", y="col2")
