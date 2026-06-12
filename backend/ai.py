import requests

MODEL = "qwen2.5:1.5b"


def ask_ai(prompt):

    try:

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        data = response.json()

        return data["response"]

    except Exception as e:

        return f"ERROR: {e}"
