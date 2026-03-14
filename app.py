import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Trader Performance vs Market Sentiment")

# Load data
data = pd.read_csv("merged_data.csv")

st.subheader("Dataset Preview")
st.dataframe(data.head())

# Sentiment distribution
st.subheader("Market Sentiment Distribution")

fig1 = plt.figure()
sns.countplot(x="classification", data=data)
plt.title("Fear vs Greed Days")

st.pyplot(fig1)


# PnL vs Sentiment
st.subheader("PnL vs Sentiment")

fig2 = plt.figure()
sns.boxplot(x="classification", y="Closed PnL", data=data)
plt.title("PnL Distribution")

st.pyplot(fig2)


# Long vs Short
st.subheader("Long vs Short Trades")

fig3 = plt.figure()
sns.countplot(x="Side", data=data)

st.pyplot(fig3)


# Trade Size Distribution
st.subheader("Trade Size Distribution")

fig4 = plt.figure()
sns.histplot(data["Size USD"], bins=40)

st.pyplot(fig4)


st.write("Dashboard created for Primetrade.ai Internship Assignment")