import streamlit as st

st.set_page_config(page_title="Games")
st.title("🎮 Mini Game: Math Challenge")

st.write("What is 7 x 8?")
answer = st.number_input("Your Answer", step=1)
if st.button("Submit Answer"):
    if answer == 56:
        st.success("Correct! 🎉 You earned 5 points.")
        st.session_state.points += 5
    else:
        st.error("Oops! Try again.")