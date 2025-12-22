from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *

DB_NAME = "kc.db"


def db_setup():
    con = None
    try:
        con = connect(DB_NAME)
        sql = "create table if not exists student(name text, language text)"
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        if con:
            con.rollback()
        print("Issue:", e)
    finally:
        if con:
            con.close()
            
db_setup()

def save():
    name = ent_name.get().strip()


    if name == "":
        showerror("Error", "Name cannot be empty or only spaces")
        ent_name.focus()
        return

    if not name.replace(" ", "").isalpha():
        showerror("Error", "Name must contain only alphabets")
        ent_name.focus()
        return

   
    languages = ""
    if py.get() == 1:
        languages += "Python "
    if ja.get() == 1:
        languages += "Java "
    if js.get() == 1:
        languages += "JavaScript "

    if languages == "":
        showerror("Error", "Please select at least one language")
        return

    con = None
    try:
        con = connect(DB_NAME)
        sql = "insert into student values(?, ?)"
        cursor = con.cursor()
        cursor.execute(sql, (name, languages))
        con.commit()

        showinfo("Success", "Data saved successfully")

        ent_name.delete(0, END)
        py.set(0)
        ja.set(0)
        js.set(0)
        ent_name.focus()

    except Exception as e:
        if con:
            con.rollback()
        showerror("Database Error", e)

    finally:
        if con:
            con.close()


root = Tk()
root.title("App by Kamal Sir")
root.geometry("1000x600+300+30")
f = ("Arial", 30, "bold")

py, ja, js = IntVar(), IntVar(), IntVar()

lab_header = Label(root, text="Language You Know App", font=f)
lab_name = Label(root, text="Enter Name", font=f)
ent_name = Entry(root, bd=3, font=f)

lab_select = Label(root, text="Select Languages", font=f)
cb_py = Checkbutton(root, text="Python", font=f, variable=py)
cb_ja = Checkbutton(root, text="Java", font=f, variable=ja)
cb_js = Checkbutton(root, text="JavaScript", font=f, variable=js)

btn_submit = Button(root, text="Submit", font=f, command=save)

lab_header.place(x=300, y=10)
lab_name.place(x=50, y=100)
ent_name.place(x=400, y=100)

lab_select.place(x=50, y=200)
cb_py.place(x=400, y=200)
cb_ja.place(x=400, y=270)
cb_js.place(x=400, y=340)

btn_submit.place(x=400, y=450)

root.mainloop()
