import streamlit as st

st.set_page_config(page_title="Home")
st.title(f"🏠 Welcome, {st.session_state.get('name', 'Student')}!")
st.subheader("Choose an activity")

col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/games.py", label="🎮 Play Games")
with col2:
    st.page_link("pages/puzzles.py", label="🧩 Try Puzzles")
with col3:
    st.page_link("pages/coding.py", label="👨‍💻 Coding Tutor")

st.markdown(f"🎯 **Your Points**: {st.session_state.get('points', 0)}")
if st.button("🚪 Logout"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("main.py")