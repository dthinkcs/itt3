
import sqlite3
conn = sqlite3.connect('users.db')

conn.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        username TEXT NOT NULL,
        password TEXT NOT NULL);
''')
conn.execute("INSERT INTO users (username, password) VALUES ('rraj', '12345');")
conn.commit()
conn.close()
