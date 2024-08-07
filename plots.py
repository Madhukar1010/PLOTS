import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

chart_data = pd.DataFrame(np.random.randn(20,3),
                          columns = ["Line1", "line2", "line3"])
st.subheader("Table of chart_data")
st.table(chart_data)

st.header("1. charts with random numbers")
st.subheader("1.1 Line chart")
st.line_chart(chart_data)

st.subheader("1.2 Area chart")
st.area_chart(chart_data)

st.subheader("1.3 Bar chart")
st.bar_chart(chart_data)

st.header("2. Visualization with matplotlib and seabron ")
st.subheader("2.1 Loading the DataFrame")
df = pd.read_csv("iris.csv")
st.table(df.head())

st.subheader("2.2 Bar graph with matplotlib")
fig = plt.figure(figsize = (15,8))
df["variety"].value_counts().plot(kind = "bar")
st.pyplot(fig)

st.subheader("2.3 Distribution plot with seabron")
fig = plt.figure(figsize = (15,8))
sns.distplot(df["sepal.length"])
st.pyplot(fig)

st.header("3. Multiple Graphs")

col1, col2 = st.columns(2)

with col1:
    fig = plt.figure(figsize = (5,5))
    sns.distplot(df["sepal.length"])
    st.pyplot(fig)
#by default kde = True and hist = True
with col2:
    col2.header = "Hist = False"
    fig = plt.figure(figsize = (5,5))
    sns.distplot(df["sepal.length"], hist = False)
    st.pyplot(fig)

st.header("4. changing style ")
col1, col2 = st.columns(2)
with col1:
    fig = plt.figure(figsize = (5,5))
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    sns.distplot(df["petal.length"], hist = False)
    st.pyplot(fig)
with col2:
    fig = plt.figure(figsize = (5,5))
    sns.set_theme(context = "notebook", style = "darkgrid")
    sns.distplot(df["petal.length"], hist = False)
    st.pyplot(fig)

st.header("5. Exploring different graphs")
st.subheader("5.1 scatter plot ")
fig = plt.figure(figsize = (15,8))
plt.scatter(np.random.randn(1000), np.random.randn(1000))
st.pyplot(fig)

st.subheader("5.2 count-plot ")
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df, x = "variety")
st.pyplot(fig)

st.subheader("5.3 box-plot ")
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x = "variety", y = "petal.length")
st.pyplot(fig)

st.subheader("5.4 violin-plot ")
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = "variety", y = "petal.length")
st.pyplot(fig)

st.write(df["variety"].value_counts())
col1, col2 = st.columns(2)
with col1:
    fig = plt.figure(figsize = (5,5))
    df["variety"].value_counts().plot(kind = "bar") #matplotlib
    st.pyplot(fig)
with col2:
    fig = plt.figure(figsize = (5,5))
    sns.countplot(data = df, x = "variety")         #using seaborn
    st.pyplot(fig)
