import sqlite3

DB_NAME = "student.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS quiz_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        subject TEXT,
        score INTEGER
    )
    """)

    conn.commit()

    conn.close()


def save_score(topic, subject, score):

    conn = sqlite3.connect(DB_NAME)

    c = conn.cursor()

    c.execute(
        "INSERT INTO quiz_history (topic, subject, score) VALUES (?, ?, ?)",
        (topic, subject, score)
    )

    conn.commit()

    conn.close()


def get_weak_topics():

    conn = sqlite3.connect(DB_NAME)

    c = conn.cursor()

    c.execute("""
    SELECT topic, AVG(score)
    FROM quiz_history
    GROUP BY topic
    ORDER BY AVG(score) ASC
    LIMIT 5
    """)

    rows = c.fetchall()

    conn.close()

    return rows
