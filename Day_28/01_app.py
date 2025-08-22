import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


st.title("Hye Guys! This is Samad")
st.markdown(" # My_First_App")
st.subheader("This is my first app")
df=sns.load_dataset("tips")
st.write(df.head())

fig=px.scatter(df,x="total_bill",y="tip",color="sex")
st.plotly_chart(fig)

plt.figure(figsize=(10,6))
sns.scatterplot(x="total_bill",y="tip",hue="sex",data=df)
st.pyplot()


# Create a scatter plot of total bill vs tip
fig1, ax = plt.subplots()
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day', ax=ax)

# Title and labels
ax.set_title('Scatter Plot of Total Bill vs Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

# Display the plot in Streamlit
st.pyplot(fig1)

# Create a pairplot
pairplot_fig = sns.pairplot(df, hue='day')

# Display the pairplot in Streamlit
st.pyplot(pairplot_fig)

# Just add it after st.sidebar:
st.radio("Select one:", [1, 2])

st.button("Click me")
# st.download_button("Download file", df, file_name="tips")
# st.link_button("Go to gallery", url)
# st.page_link("app.py", label="Home")
# st.data_editor("Edit data", df)
st.checkbox("I agree")
st.feedback("thumbs")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.audio_input("Record a voice message")
st.camera_input("Take a picture")
st.color_picker("Pick a color")







