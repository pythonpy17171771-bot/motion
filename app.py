import streamlit as st

st.set_page_config(
    page_title="감쇠 조화 운동 보여주기",
    layout="wide"
)
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

st.components.v1.html(html_data, height=1000, scrolling=True)
