import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        name TEXT,
        password TEXT,
        grade TEXT,
        points INTEGER DEFAULT 0
    )''')
    conn.commit()
    conn.close()

def add_user(name, email, password, grade):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email, password, grade) VALUES (?, ?, ?, ?)", (name, email, password, grade))
    conn.commit()
    conn.close()

def get_user(email, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    conn.close()
    return user

def update_points(email, points):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("UPDATE users SET points=? WHERE email=?", (points, email))
    conn.commit()
    conn.close()