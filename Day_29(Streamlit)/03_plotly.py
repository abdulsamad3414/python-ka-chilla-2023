import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

# import dataset
st.header("Plotly and streamlit integration")
df=px.data.gapminder()
st.write(df.head())
st.write(df.columns) # df.columns

# summary stats 
st.write(df.describe())

#Data management
year_option=df["year"].unique().tolist()
year=st.selectbox("Select year",year_option)
# df=df[df["year"]==year]

#plot
fig=px.scatter(df,x="gdpPercap",y="lifeExp",size="pop",color="continent",hover_name="country",log_x=True,size_max=60,animation_frame="year",animation_group="country",range_x=[100,100000],range_y=[20,90])
fig.update_layout(title="Scatter plot",xaxis_title="GDP per capita",yaxis_title="Life Expectancy")
fig.update_layout(template="plotly_dark")
fig.update_layout(height=600,width=800)
st.write(fig)

