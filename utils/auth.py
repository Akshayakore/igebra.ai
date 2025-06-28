import streamlit as st
from utils.database import add_user, get_user

def login_user():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user(email, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.email = user[0]
            st.session_state.name = user[1]
            st.session_state.grade = user[3]
            st.session_state.points = user[4]
            st.switch_page("pages/home.py")
        else:
            st.error("Invalid login")

def signup_user():
    st.subheader("Sign Up")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    grade = st.selectbox("Grade", [str(i) for i in range(4, 11)])
    if st.button("Create Account"):
        try:
            add_user(name, email, password, grade)
            st.success("Account created! Please log in.")
        except:
            st.error("Account with this email already exists.")