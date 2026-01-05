from bottle import *
from sqlite3 import *

def db_setup():
    con = connect("wn.db")
    cursor = con.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS student (name TEXT, choice TEXT)"
    )
    con.commit()
    con.close()

db_setup()

application = Bottle()

@application.route("/")
def home():
    con = connect("wn.db")
    cursor = con.cursor()
    cursor.execute("SELECT name, choice FROM student")
    data = cursor.fetchall()
    con.close()
    return template("home", msg=data)

@application.route("/whatnext", method=["GET", "POST"])
def whatnext():
    if request.method == "POST":
        name = request.forms.get("name")
        choice = request.forms.get("choice")

        con = connect("wn.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO student VALUES (?,?)", (name, choice))
        con.commit()
        con.close()

        return template("whatnext", msg="OK Noted")
    return template("whatnext", msg="")
