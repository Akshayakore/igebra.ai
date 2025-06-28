import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("gemini_api_key"))

def extract_hints(response_text):
    hints = []
    for level in range(1, 4):
        marker = f"**Level {level} Hint**:"
        if marker in response_text:
            start = response_text.index(marker) + len(marker)
            end = response_text.find("**Level", start)
            hint = response_text[start:end].strip() if end != -1 else response_text[start:].strip()
            hints.append(hint)
    return hints

def get_full_feedback_with_hints(question, user_code):
    prompt = f"""
    You are an AI tutor for kids learning to code.

    Problem:
    {question}

    Code:
    ```python
    {user_code}
    ```

    Rules:
    - If correct: Appreciate & explain time complexity.
    - If wrong: Give 3 hint levels.

    Response Format:
    - Only hints or appreciation.
    """
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text

def get_optimal_solution(question):
    prompt = f"""
    You are a tutor for young coders.

    Problem:
    {question}

    Show best Python solution with time/space complexity. No markdown.
    """
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text