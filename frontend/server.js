const express = require("express")

const { spawn } = require("child_process")

const app = express()

app.use(express.json())

app.use(express.static("public"))

function runPython(mode, data, res) {

    const py = spawn(
        "python",
        [
            "../backend/web_api.py",
            mode,
            JSON.stringify(data)
        ]
    )

    let output = ""

    py.stdout.on("data", (data) => {

        output += data.toString()

    })

    py.stderr.on("data", (data) => {

        output += data.toString()

    })

    py.on("close", () => {

        res.json({
            response: output
        })

    })
}

const modes = [
    "ask",
    "quiz",
    "answer",
    "flashcards",
    "reveal",
    "study",
    "recommend"
]

for (const mode of modes) {

    app.post(`/api/${mode}`, (req, res) => {

        runPython(mode, req.body, res)

    })

}

app.listen(3000, () => {

    console.log(
        "StudyBuddy running at http://localhost:3000"
    )

})
