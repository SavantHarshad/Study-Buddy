import os


def speak(text):

    safe_text = text.replace('"', "")

    os.system(
        f'termux-tts-speak "{safe_text}"'
    )
