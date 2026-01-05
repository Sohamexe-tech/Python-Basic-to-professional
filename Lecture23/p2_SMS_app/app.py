from bottle import *
from sqlite3 import *
import re

def db_setup():
    con = None
    try:
        con = connect("sms.db")
        cursor = con.cursor()
        cursor.execute("create table if not exists student (rno int primary key, name text, marks int)")
        con.commit()
    except:
        if con:
            con.rollback()
    finally:
        if con:
            con.close()

db_setup()

application = Bottle()

@application.route("/")
def home():
    con = None
    try:
        con = connect("sms.db")
        cursor = con.cursor()
        cursor.execute("select rno, name, marks from student")
        data = cursor.fetchall()
        return template("home", msg=data)
    except:
        return template("home", msg=[])
    finally:
        if con:
            con.close()

@application.route("/create", method=["GET", "POST"])
def create():
    if request.method == "POST":
        rno = request.forms.get("rno")
        name = request.forms.get("name")
        marks = request.forms.get("marks")

        if rno == "" or name == "" or marks == "":
            return template("create", msg="All fields required")

        if not re.fullmatch(r"[0-9]+", rno):
            return template("create", msg="Invalid Roll No")

        if not re.fullmatch(r"[A-Za-z ]+", name):
            return template("create", msg="Invalid Name")

        if not re.fullmatch(r"[0-9]+", marks):
            return template("create", msg="Invalid Marks")

        rno = int(rno)
        marks = int(marks)

        if marks < 0 or marks > 100:
            return template("create", msg="Marks must be 0 to 100")

        con = None
        try:
            con = connect("sms.db")
            cursor = con.cursor()
            cursor.execute("insert into student values (?,?,?)", (rno, name.strip(), marks))
            con.commit()
            return template("create", msg="Saved Successfully")
        except:
            return template("create", msg="Roll No Exists")
        finally:
            if con:
                con.close()

    return template("create", msg="")

@application.route("/delete/<r:int>", method=["GET", "POST"])
def delete(r):
    if request.method == "POST":
        rno = request.forms.get("rno")
        con = None
        try:
            con = connect("sms.db")
            cursor = con.cursor()
            cursor.execute("delete from student where rno=?", (int(rno),))
            con.commit()
            return template("delete", msg="Deleted", data="")
        except:
            return template("delete", msg="Issue", data="")
        finally:
            if con:
                con.close()

    return template("delete", msg="", data=r)

@application.route("/update/<r:int>", method=["GET", "POST"])
def update(r):
    if request.method == "POST":
        rno = request.forms.get("rno")
        name = request.forms.get("name")
        marks = request.forms.get("marks")

        if rno == "" or name == "" or marks == "":
            return template("update", msg="All fields required", data=None)

        if not re.fullmatch(r"[A-Za-z ]+", name):
            return template("update", msg="Invalid Name", data=None)

        if not re.fullmatch(r"[0-9]+", marks):
            return template("update", msg="Invalid Marks", data=None)

        marks = int(marks)

        if marks < 0 or marks > 100:
            return template("update", msg="Marks must be 0 to 100", data=None)

        con = None
        try:
            con = connect("sms.db")
            cursor = con.cursor()
            cursor.execute("update student set name=?, marks=? where rno=?", (name.strip(), marks, int(rno)))
            con.commit()
            return template("update", msg="Updated Successfully", data=None)
        except:
            return template("update", msg="Issue", data=None)
        finally:
            if con:
                con.close()

    con = None
    try:
        con = connect("sms.db")
        cursor = con.cursor()
        cursor.execute("select rno, name, marks from student where rno=?", (r,))
        data = cursor.fetchone()
        return template("update", msg="", data=data)
    except:
        return template("update", msg="Issue", data=None)
    finally:
        if con:
            con.close()

#run(application, debug=True, use_reloader=True, port=4050)
