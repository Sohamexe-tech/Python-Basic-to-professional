from bottle import Bottle, run, template, request, redirect
import sqlite3

app = Bottle()

# ---------- DATABASE CONNECTION ----------

def get_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students(
            rollno INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_table()

# ---------- HOME (READ) ----------

@app.route('/')
def index():
    conn = get_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return template("index", students=students)

# ---------- CREATE ----------

@app.route('/create')
def create():
    return template("create")

@app.route('/create', method="POST")
def save_student():
    rollno = request.forms.get("rollno")
    name = request.forms.get("name")
    marks = request.forms.get("marks")

    # VALIDATION
    if not rollno.isdigit():
        return "<h3>Roll No must be numeric!</h3>"

    if not marks.isdigit():
        return "<h3>Marks must be numeric!</h3>"

    if not name.replace(" ", "").isalpha():
        return "<h3>Name must contain only alphabets!</h3>"

    if int(marks) < 0 or int(marks) > 100:
        return "<h3>Marks must be between 0 and 100!</h3>"

    try:
        conn = get_connection()
        conn.execute("INSERT INTO students VALUES (?, ?, ?)",
                     (int(rollno), name, int(marks)))
        conn.commit()
        conn.close()
        redirect('/')
    except sqlite3.IntegrityError:
        return "<h3>Roll No already exists!</h3>"

# ---------- UPDATE ----------

@app.route('/update/<rollno>')
def edit(rollno):
    conn = get_connection()
    student = conn.execute("SELECT * FROM students WHERE rollno=?",
                           (rollno,)).fetchone()
    conn.close()
    return template("update", student=student)

@app.route('/update/<rollno>', method="POST")
def update_student(rollno):
    name = request.forms.get("name")
    marks = request.forms.get("marks")

    if not marks.isdigit():
        return "<h3>Marks must be numeric!</h3>"

    if not name.replace(" ", "").isalpha():
        return "<h3>Name must contain only alphabets!</h3>"

    conn = get_connection()
    conn.execute("UPDATE students SET name=?, marks=? WHERE rollno=?",
                 (name, int(marks), rollno))
    conn.commit()
    conn.close()
    redirect('/')

# ---------- DELETE ----------

@app.route('/delete/<rollno>')
def delete(rollno):
    conn = get_connection()
    conn.execute("DELETE FROM students WHERE rollno=?",
                 (rollno,))
    conn.commit()
    conn.close()
    redirect('/')

# ---------- RUN ----------

run(app, host="localhost", port=8080, debug=True)
