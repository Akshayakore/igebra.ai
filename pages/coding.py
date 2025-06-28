import streamlit as st
from streamlit_ace import st_ace
import subprocess
from llm import get_full_feedback_with_hints, extract_hints, get_optimal_solution
from utils.database import update_points

st.set_page_config(page_title="DSA Coding Tutor", layout="wide")
st.title("👨‍💻 DSA Code Tutor with AI")

problems = {
    "Maximum Product Subarray": "Given an integer array nums...",
    "Longest Palindromic Substring": "Given a string s, return..."
}
options = ["Select"] + list(problems.keys())
selected = st.selectbox("Choose a problem", options)
if selected != "Select":
    st.session_state["problem"] = problems[selected]

problem = st.text_area("✍️ Problem", value=st.session_state.get("problem", ""), height=150)
st.subheader("✏️ Your Code")
code = st_ace(language="python", theme="monokai", font_size=14)

if st.button("Run Code"):
    if code:
        with open("temp_code.py", "w") as f:
            f.write(code)
        result = subprocess.run(["python", "temp_code.py"], capture_output=True, text=True)
        st.text_area("📄 Output", value=result.stdout or "(No output)", height=200)
        if result.stderr:
            st.error(result.stderr)

if st.button("🔍 Get AI Feedback"):
    if code and problem:
        feedback = get_full_feedback_with_hints(problem, code)
        hints = extract_hints(feedback)
        if hints:
            st.markdown(f"**Level 1 Hint**: {hints[0]}")
            if len(hints) > 1 and st.button("Level 2 Hint"):
                st.markdown(f"**Level 2 Hint**: {hints[1]}")
            if len(hints) > 2 and st.button("Level 3 Hint"):
                st.markdown(f"**Level 3 Hint**: {hints[2]}")
        else:
            st.success("✅ Looks great! +10 points!")
            st.session_state.points += 10
            update_points(st.session_state.email, st.session_state.points)

if st.button("📘 Show Optimal Solution"):
    if problem:
        solution = get_optimal_solution(problem)
        st.text_area("Optimal Solution", value=solution, height=300)