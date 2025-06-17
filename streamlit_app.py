import streamlit as st

st.set_page_config(page_title="CheckCheckCheck", layout="wide")

# --- 初始化用户字典 ---
if 'users' not in st.session_state:
    st.session_state['users'] = {"admin": "123456"}

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

if not st.session_state['logged_in']:
    login()
else:
    st.sidebar.title("管理菜单")
    option = st.sidebar.selectbox("选择操作", ["主页", "添加用户", "退出登录"])

    if option == "主页":
        # 读取本地 HTML 文件内容
        with open("index.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        st.title("🔗 CheckCheckCheck")
        st.components.v1.html(html_content, height=800, scrolling=True)

    elif option == "添加用户":
        add_user()

    elif option == "退出登录":
        st.session_state['logged_in'] = False
        st.experimental_rerun()
