# import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Containers
header = st.container()
data_set = st.container()
feature = st.container()
model_training = st.container()

with header:
    st.title("Kashti App")
    st.text("In this Dataset we will work on Titanic dataset")

with data_set:
    st.header("Kashti Doob Gai Haww!")
    st.text("We will work with Titanic dataset")
    df = sns.load_dataset("titanic")
    df.dropna(inplace=True)  # drop missing values
    st.write(df.head())

    fig = px.bar(df, x="sex", y="survived")
    st.plotly_chart(fig)

    df["sex"].value_counts().plot.pie(autopct="%1.1f%%")
    st.pyplot(plt.gcf())
    plt.clf()  # clear figure after plotting

with feature:
    st.header("These are my App features")
    st.text("1. Feature 1")
    st.text("2. Feature 2")
    st.text("3. Feature 3")
    st.text("4. Feature 4")

with model_training:
    st.header("Kashti walo ka kya bana?")
    st.text("We will train a model in this app")

    st.bar_chart(df["survived"].value_counts())

    # Columns for input and output
    input_col, display_col = st.columns(2)

    with input_col:
        num_people = st.select_slider("How many people are there?", options=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        n_estimators = st.selectbox("Select n_estimators", [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        max_depth = st.selectbox("Select max_depth", [5, 10, 15, 20, None])

        # Select numeric features only
        numeric_features = df.select_dtypes(include=[np.number]).columns.tolist()
        input_features = st.selectbox("Select input feature", numeric_features)

    # Model
    X = df[[input_features]]
    y = df[["fare"]]

    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X, y)

    predictions = model.predict(X)

    with display_col:
        st.subheader("Predictions")
        st.write(predictions[:10])  # show first 10 predictions

        st.subheader("Model Scores")
        st.write("R2 Score:", r2_score(y, predictions))
        st.write("Mean Squared Error:", mean_squared_error(y, predictions))
        st.write("Mean Absolute Error:", mean_absolute_error(y, predictions))
