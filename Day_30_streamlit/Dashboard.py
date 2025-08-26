import pandas as pd
import Day_30_streamlit.Dashboard as st
from sklearn.ensemble import RandomForestClassifier

st.write(" # Random forest Classification App")
st.subheader("**Made By Abdul Samad**")
st.subheader("This app is made for prediction of iris Dataset")
st.sidebar.header("Change Iris Parameters")
def user_input_feature():
    sepel_length= st.sidebar.slider("Sepel Length", 4.3, 7.9, 5.4) # means start with 5.4 
    sepel_width = st.sidebar.slider("Sepel Width", 2.0, 4.4, 3.4) # start with 3.4
    petal_length = st.sidebar.slider("Petal Length", 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)
    data = {"sepal_length": sepel_length,
            "sepal_width": sepel_width,
            "petal_length": petal_length,
            "petal_width": petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_feature()
st.write("Iris parameters")
st.write(df)
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
iris = sns.load_dataset("iris")
st.header("Iris Dataset")
st.write(iris.head())
st.bar_chart(iris["species"].value_counts(), height=500, width=600, use_container_width=True)
st.subheader("Iris Scatter plot by Plotly")
fig=px.scatter(iris,x="sepal_length",y="sepal_width",color="species")
st.plotly_chart(fig)
fig=px.bar_polar(iris, r="sepal_length", theta="species", color="species")
st.plotly_chart(fig)
st.subheader ("Iris Scatter plot 3D by Plotly")
fig=px.scatter_3d(iris,x="sepal_length",y="sepal_width",z="petal_length",color="species")
st.plotly_chart(fig)
# fig=plt.figure(figsize=(10,6))
# st.subheader("Iris Bar plot by Seaborn")
# sns.barplot(x="species", y="sepal_length", data=iris,hue="species")
# st.pyplot()
X = iris.drop("species", axis=1)
Y = iris["species"]
model= RandomForestClassifier()
model.fit(X, Y)
prediction = model.predict(df)
st.subheader("Class labels and their corresponding index number")
st.write(iris["species"].unique())
st.subheader("Prediction")
st.write(prediction)
st.subheader("Prediction Probablity")
st.write(model.predict_proba(df))
