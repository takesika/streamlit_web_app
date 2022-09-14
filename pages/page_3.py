
import streamlit as st
import pandas as pd
df = pd.read_csv('data/iris.csv')
st.bar_chart(df)

