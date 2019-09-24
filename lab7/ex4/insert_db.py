import sqlite3

conn = sqlite3.connect('studentCourses.db')

#conn.execute("""
#conn.execute("INSERT INTO students (name, cgpa) VALUES ('Rishabh Raj Jaiswal', 8.67);")
#conn.execute("INSERT INTO students (name, cgpa) VALUES ('Aditi Goyal', 8.66);")
conn.execute("INSERT INTO students (name, cgpa) VALUES ('Sarathkrishnan Ramesh', 8.73);")
conn.execute("INSERT INTO students (name, cgpa) VALUES ('Tejas Kashinath', 8.85);")
conn.execute("INSERT INTO students (name, cgpa) VALUES ('Nipun Ramani', 7.4);")
conn.execute("INSERT INTO students (name, cgpa) VALUES ('Bhavik Munot', 8.73);")

conn.commit()
conn.close()
