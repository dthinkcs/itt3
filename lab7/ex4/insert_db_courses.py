import sqlite3

conn = sqlite3.connect('studentCourses.db')

conn.execute("INSERT INTO courses VALUES ('Tech101', 'Data Structures Algorithms Competitive Programming') ")
conn.execute("INSERT INTO courses VALUES ('Tech102', 'Application Development and System Design')")
conn.execute("INSERT INTO courses VALUES ('Tech103', 'Artificial Intelligence Machine Learning Data Science')")

conn.commit()
conn.close()
