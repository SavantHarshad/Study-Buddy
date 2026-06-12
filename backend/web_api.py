import sys

from ai import ask_ai

mode = sys.argv[1]

if mode == "ask":

    question = sys.argv[2]

    prompt = f"""
You are a tutor.

Question:
{question}

Answer simply.
"""

    print(
        ask_ai(prompt)
    )
