let currentMode = "ask"

function setMode(mode) {

    currentMode = mode

    const title =
        mode.charAt(0).toUpperCase() +
        mode.slice(1)

    document.getElementById(
        "modeTitle"
    ).innerText =
        `${title} Mode`

    const placeholders = {

        ask:
            "Ask any question...",

        quiz:
            "Enter quiz topic...",

        answer:
            "Enter your quiz answer...",

        flashcards:
            "Enter flashcard topic...",

        reveal:
            "Reveal flashcard answer...",

        study:
            "Enter chapter/topic...",

        recommend:
            "Get study recommendations..."
    }

    document.getElementById(
        "inputBox"
    ).placeholder =
        placeholders[mode] || "Type here..."
}

async function runMode() {

    const input =
        document.getElementById(
            "inputBox"
        ).value

    const subject =
        document.getElementById(
            "subject"
        ).value

    const difficulty =
        document.getElementById(
            "difficulty"
        ).value

    const language =
        document.getElementById(
            "language"
        ).value

    const bilingual =
        document.getElementById(
            "bilingual"
        ).checked

    const voice =
        document.getElementById(
            "voice"
        ).checked

    const output =
        document.getElementById(
            "output"
        )

    output.innerText =
        "Thinking..."

    try {

        const response = await fetch(
            `/api/${currentMode}`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    input,
                    subject,
                    difficulty,
                    language,
                    bilingual,
                    voice
                })
            }
        )

        const data =
            await response.json()

        output.innerText =
            data.response

    } catch (err) {

        output.innerText =
            "Error connecting to backend."
    }
}
