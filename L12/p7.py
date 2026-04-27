from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *

def db_setup():
    con = None
    try:
        con = connect("food.db")
        sql = "CREATE TABLE IF NOT EXISTS person(name TEXT, choice TEXT)"
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print("issue", e)
        if con:
            con.rollback()
    finally:
        if con:
            con.close()

db_setup()

def save():
    name = ent_name.get()

    if name == "":
        showerror("Name issue", "Name should not be empty")
        ent_name.focus()
        return

    if c.get() == 1:
        choice = "North Indian"
    elif c.get() == 2:
        choice = "South Indian"
    else:
        choice = "Fast Food"

    con = None
    try:
        con = connect("food.db")
        sql = "INSERT INTO person VALUES (?, ?)"
        cursor = con.cursor()
        cursor.execute(sql, (name, choice))
        con.commit()
        showinfo("Saved", "Noted Successfully")
        ent_name.delete(0, END)
        c.set(1)
        ent_name.focus()
    except Exception as e:
        showerror("DB Error", e)
        if con:
            con.rollback()
    finally:
        if con:
            con.close()

root = Tk()
root.title("Food You Like App by Soham Dalvi")
root.geometry("1000x650+300+30")
f = ("Times New Roman", 30, "bold")

lab_header = Label(root, text="Food You Like App", font=f)
lab_header.place(x=300, y=20)

lab_name = Label(root, text="Enter Name", font=f)
ent_name = Entry(root, bd=3, font=f)
lab_name.place(x=50, y=100)
ent_name.place(x=400, y=100)

c = IntVar()
c.set(1)

lab_select = Label(root, text="Select One", font=f)
rb_ni = Radiobutton(root, text="North Indian", font=f, variable=c, value=1)
rb_si = Radiobutton(root, text="South Indian", font=f, variable=c, value=2)
rb_ff = Radiobutton(root, text="Fast Food", font=f, variable=c, value=3)

lab_select.place(x=50, y=200)
rb_ni.place(x=400, y=200)
rb_si.place(x=400, y=270)
rb_ff.place(x=400, y=340)

btn_submit = Button(root, text="Submit", font=f, command=save)
btn_submit.place(x=400, y=450)

ent_name.focus()
root.mainloop()
