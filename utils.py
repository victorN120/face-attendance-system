import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS attendance (
                    name TEXT,
                    time TEXT
                )''')
    conn.commit()
    conn.close()

def mark_attendance(name):
    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO attendance (name, time) VALUES (?, ?)",
                (name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()