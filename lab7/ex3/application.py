import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)
conn = sqlite3.connect("users.db")
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        rows = conn.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}' ;".format(username, password))
        length = 0
        for row in rows:
            length += 1
        #if len(rows) == 0:
        if length != 1:
            return "<h1>INVALID USERNAME or PASSWORD</h1>"
        else:
            return "<h1>WELCOME</h1>"
