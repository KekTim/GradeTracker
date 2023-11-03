import sqlite3

with sqlite3.connect("database.db") as connection:
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT NOT NULL,
                    username TEXT NOT NULL,
                    image TEXT NOT NULL,
                    password_hash TEXT NOT NULL,
                    session_token TEXT NOT NULL,
                    UNQIUE (username),
                    UNIQUE (session_token),
                    PRIMARY KEY (user_id)
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS subjects (
                    user_id TEXT NOT NULL,
                    subject_id TEXT NOT NULL,
                    name TEXT NOT NULL,
                    description TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE,
                    PRIMARY KEY (subject_id),
                    UNIQUE (user_identifier, name)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS exams (
                    user_id TEXT NOT NULL,
                    subject_id TEXT NOT NULL,
                    exam_id TEXT NOT NULL,
                    grade INTEGER NOT NULL,
                    weight FLOAT NOT NULL,
                    type TEXT,
                    date DATE,
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON UPDATE CASCADE ON DELETE CASCADE,
                    PRIMARY KEY (exam_id)
    )""")
    
    cursor.close()
    connection.commit()
