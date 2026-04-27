from bottle import *
from sqlite3 import *
import re

app = Bottle()

def db_setup():
    with connect("lang.db") as con:
        cur = con.cursor()
        cur.execute(
            "create table if not exists person (name text, language text)"
        )

db_setup()

@app.route("/")
def home():
    with connect("lang.db") as con:
        cur = con.cursor()
        cur.execute("select * from person")
        data = cur.fetchall()
    return template("home.tpl", msg=data)

@app.route("/language", method=["GET", "POST"])
def language():
    if request.method == "POST":
        name = request.forms.get("name", "").strip()

        if not name:
            return template("language.tpl", msg="Name cannot be empty")

        if not re.fullmatch(r"[A-Za-z ]+", name):
            return template(
                "language.tpl",
                msg="Only alphabets and spaces allowed"
            )

        langs = [
            lang for key, lang in {
                "py": "Python",
                "js": "JavaScript",
                "ja": "Java",
                "genai": "Gen AI"
            }.items()
            if request.forms.get(key)
        ]

        if not langs:
            return template(
                "language.tpl",
                msg="Please select at least one language"
            )

        language = ", ".join(langs)

        with connect("lang.db") as con:
            cur = con.cursor()
            cur.execute(
                "insert into person values (?, ?)",
                (name, language)
            )

        return template(
            "language.tpl",
            msg="Saved successfully ✔"
        )

    return template("language.tpl", msg="")

run(app, debug=True, port=4050)
