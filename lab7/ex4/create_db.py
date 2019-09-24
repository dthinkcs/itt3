
import sqlite3
conn = sqlite3.connect('studentCourses.db')

conn.execute('''
    CREATE TABLE students (
        id INT PRIMARY KEY ,
        name TEXT NOT NULL,
        cgpa REAL NOT NULL);
''')
conn.execute('''
    CREATE TABLE courses (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL
    )
''')
conn.close()
