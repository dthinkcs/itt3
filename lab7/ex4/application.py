import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)
conn = sqlite3.connect("studentCourses.db")
@app.route("/")
def index():
    q = request.args.get("q")
    if q is None:
        q = ""
    studentRows = conn.execute("SELECT * FROM students WHERE name LIKE '%{}%' ;".format(q))

    courseRows  = conn.execute("SELECT * FROM courses;")

    return render_template("index.html", studentRows=studentRows, courseRows=courseRows)
