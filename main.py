import streamlit as st
from utils.auth import login_user
from utils.database import init_db

st.set_page_config(page_title="DSA Code Tutor", layout="wide")
init_db()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("pages/home.py")
else:
    login_user()