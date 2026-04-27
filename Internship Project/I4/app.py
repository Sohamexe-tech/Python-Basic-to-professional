from bottle import Bottle, run, template, request, redirect
import sqlite3
import re

app = Bottle()
DB = "todo.db"

# ---------------- DATABASE CONNECTION ----------------
def get_connection():
    return sqlite3.connect(DB, timeout=10)

# ---------------- CREATE TABLE ----------------
def create_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_table()

# ---------------- VALIDATION ----------------
def is_valid_task(task):
    # Allow only letters, numbers, spaces
    return bool(re.fullmatch(r"[A-Za-z0-9 ]+", task))

# ---------------- HOME ----------------
@app.route("/")
def index():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return template("index", tasks=tasks)

# ---------------- CREATE ----------------
@app.route("/create", method=["GET", "POST"])
def create():
    error = ""
    if request.method == "POST":
        title = request.forms.get("title", "").strip()
        status = request.forms.get("status")

        if not title:
            error = "Task cannot be empty"
        elif not is_valid_task(title):
            error = "Only letters, numbers and spaces allowed"
        else:
            try:
                conn = get_connection()
                conn.execute(
                    "INSERT INTO tasks (title, status) VALUES (?, ?)",
                    (title, status)
                )
                conn.commit()
                conn.close()
                redirect("/")
            except sqlite3.OperationalError:
                error = "Database busy. Try again."

    return template("create", error=error)

# ---------------- UPDATE ----------------
@app.route("/update/<id>", method=["GET", "POST"])
def update(id):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    task = conn.execute("SELECT * FROM tasks WHERE id=?", (id,)).fetchone()
    conn.close()

    if not task:
        redirect("/")

    error = ""
    if request.method == "POST":
        title = request.forms.get("title", "").strip()
        status = request.forms.get("status")

        if not title:
            error = "Task cannot be empty"
        elif not is_valid_task(title):
            error = "Only letters, numbers and spaces allowed"
        else:
            try:
                conn = get_connection()
                conn.execute(
                    "UPDATE tasks SET title=?, status=? WHERE id=?",
                    (title, status, id)
                )
                conn.commit()
                conn.close()
                redirect("/")
            except sqlite3.OperationalError:
                error = "Database busy. Try again."

    return template("update", task=task, error=error)

# ---------------- DELETE ----------------
@app.route("/delete/<id>")
def delete(id):
    try:
        conn = get_connection()
        conn.execute("DELETE FROM tasks WHERE id=?", (id,))
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        pass
    redirect("/")

run(app, host="localhost", port=8080, debug=True)
