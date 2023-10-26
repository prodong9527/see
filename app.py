import streamlit as st
from streamlit_chat import message

import SparkApi
#以下密钥信息从控制台获取
appid = "5dcc9c3b"     #填写控制台中获取的 APPID 信息
api_secret = "OWExYjk3MzQzMjE3MGNjMWVhYmIwNDZm"   #填写控制台中获取的 APISecret 信息
api_key ="8868cf5443e9b63945cc9eb4187a120b"    #填写控制台中获取的 APIKey 信息

#用于配置大模型版本，默认“general/generalv2”
# domain = "general"   # v1.5版本
domain = "generalv2"    # v2.0版本
#云端环境的服务地址
# Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址

text=[]
def getText(role,content):
    jsoncon={}
    jsoncon["role"]=role
    jsoncon["content"]=content
    text.append(jsoncon)
    return text

def getlength(text):
    length=0
    for content in text:
        temp=content["content"]
        leng=len(temp)
        length+=leng
    return length

def checklen(text):
    while getlength(text)>8000:
        del text[0]
    return text



if __name__=='__main__':
    st.markdown("### 认知模型")

    if 'generated' not in st.session_state:
        st.session_state['generated']=[]
    if 'past' not in st.session_state:
        st.session_state['past']=[]

    user_input=st.text_input("问题",key='input')
    if user_input:
        question=checklen(getText("user",user_input))

        SparkApi.answer=""
        print("星火：",end="")
        SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
        output=getText("assistant",SparkApi.answer)

        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(str(output[1]['content']))

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated']) -1,-1,-1):
            message(st.session_state["generated"][i],key=str(i))
            message(st.session_state['past'][i],is_user=True,key=str(i)+'_user')