import streamlit as st

with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

st.components.v1.html(html_data, height=2000, scrolling=True)
