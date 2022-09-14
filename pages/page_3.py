
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/iris.csv')
st.bar_chart(df)

fig, ax = plt.subplots()
ax.plot(df.index)
ax.set_title('mpg')
st.pyplot(fig)