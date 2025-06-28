import streamlit as st

st.set_page_config(page_title="Puzzles")
st.title("🧩 Riddle Time!")

st.write("I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?")
guess = st.text_input("Your Answer")
if st.button("Check Answer"):
    if guess.lower().strip() == "echo":
        st.success("You're right! +5 points")
        st.session_state.points += 5
    else:
        st.warning("Nice try! Hint: It's a sound...")