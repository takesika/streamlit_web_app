import streamlit as st
from PIL import Image

st.title('アプリ')
st.caption("テストアプリです")

img = Image.open('data/vision.png')
st.image(img, width=200)
