import streamlit as st

# ✅ 这一行必须放最上面
st.set_page_config(page_title="CheckCheckCheck", layout="wide")

import streamlit as st

# 这段 CSS 会美化按钮、输入框、整体背景，简单好看
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f5;
        color: #222;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 8px 24px;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stTextInput>div>div>input {
        border: 1.5px solid #007bff;
        border-radius: 6px;
        padding: 6px 10px;
    }
    .css-1d391kg {
        max-width: 600px;
        margin: auto;
        padding: 24px;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgb(0 0 0 / 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 初始化用户字典 ---
if 'users' not in st.session_state:
    st.session_state['users'] = {"admin": "1008611"}

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    st.title("登录")
    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")
    if st.button("登录"):
        if username in st.session_state['users'] and st.session_state['users'][username] == password:
            st.session_state['logged_in'] = True
            st.success(f"欢迎 {username}！")
            st.rerun()  # ✅ 使用新版本的 rerun 方法
        else:
            st.error("用户名或密码错误")

def add_user():
    st.title("添加新用户")
    new_user = st.text_input("新用户名")
    new_pass = st.text_input("新密码", type="password")
    if st.button("添加用户"):
        if new_user in st.session_state['users']:
            st.warning("用户已存在！")
        elif new_user == "" or new_pass == "":
            st.warning("用户名和密码不能为空！")
        else:
            st.session_state['users'][new_user] = new_pass
            st.success(f"添加用户 {new_user} 成功！")

# --- 登录逻辑与页面显示 ---
if not st.session_state['logged_in']:
    login()
else:
    st.sidebar.title("管理菜单")
    option = st.sidebar.selectbox("选择操作", ["主页", "添加用户", "退出登录"])

    if option == "主页":
        st.title("🔗 CheckCheckCheck")
        try:
            with open("index.html", "r", encoding="utf-8") as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=800, scrolling=True)
        except FileNotFoundError:
            st.error("找不到 index.html 文件，请确保文件存在于项目目录中。")

    elif option == "添加用户":
        add_user()

    elif option == "退出登录":
        st.session_state['logged_in'] = False
        st.rerun()  # ✅ 替代 experimental_rerun()
