import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 加载内置数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建逻辑回归模型
model = LogisticRegression()

# 训练模型
model.fit(X_train, y_train)

# 显示训练数据集
st.write("训练数据集：")
st.write(X_train)

# 用户输入特征
input_features = []
for feature in iris.feature_names:
    input_value = st.number_input(f"请输入{feature}的值：", value=0.0)
    input_features.append(input_value)

# 将输入的特征转换为数组
input_features = np.array(input_features).reshape(1, -1)

# 进行预测
prediction = model.predict(input_features)

# 显示预测结果
st.write(f"预测结果：{iris.target_names[prediction][0]}")
