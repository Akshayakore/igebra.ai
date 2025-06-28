import streamlit as st
from utils.auth import signup_user, login_user

st.title("🔐 Welcome to DSA Tutor")
tab1, tab2 = st.tabs(["Login", "Sign Up"])

with tab1:
    login_user()

with tab2:
    signup_user()