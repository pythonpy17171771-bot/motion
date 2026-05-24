import streamlit as st

# Streamlit 화면 설정
st.set_page_config(
    page_title="감쇠 조화 운동 증명",
    layout="wide"
)

# HTML 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 제목
st.title("복소수와 감쇠 조화 운동")

# HTML 출력
st.components.v1.html(
    html_data,
    height=9000,
    scrolling=True
)
