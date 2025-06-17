import streamlit as st

# 读取本地 HTML 文件内容
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.set_page_config(page_title="CheckCheckCheck", layout="wide")

st.title("🔗 CheckCheckCheck")

# 嵌入完整 HTML 页面（允许执行其中 JS）
st.components.v1.html(html_content, height=800, scrolling=True)
