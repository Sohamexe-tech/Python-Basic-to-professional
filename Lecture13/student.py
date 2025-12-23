from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def db_setup():
    con = None
    try:
        con = connect("sms.db")
        sql = "create table if not exists student(rno int primary key, name text)"
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        if con:
            con.rollback()
        print("issue", e)
    finally:
        if con:
            con.close()

db_setup()

def save():
    try:
        rno = aw_ent_rno.get().strip()
        name = aw_ent_name.get().strip()

        
        if rno == "":
            raise Exception("Roll number cannot be blank")
        if not rno.isdigit():
            raise Exception("Roll number must contain only numbers")

        # Name validation
        if name == "":
            raise Exception("Name cannot be blank")
        if not name.replace(" ", "").isalpha():
            raise Exception("Name must contain only alphabets")

        rno = int(rno)

        con = connect("sms.db")
        cursor = con.cursor()
        sql = "insert into student values(?, ?)"
        cursor.execute(sql, (rno, name))
        con.commit()

        showinfo("Success", "Record Created Successfully")

        aw_ent_rno.delete(0, END)
        aw_ent_name.delete(0, END)
        aw_ent_rno.focus()

    except Exception as e:
        showerror("Error", e)

    finally:
        if 'con' in locals():
            con.close()


def view():
    vw_st_data.delete(0.0, END)
    try:
        con = connect("sms.db")
        cursor = con.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        data = cursor.fetchall()

        for d in data:
            vw_st_data.insert(INSERT, f"Rno = {d[0]}   Name = {d[1]}\n")

    except Exception as e:
        showerror("Error", e)

    finally:
        if 'con' in locals():
            con.close()


def mw_to_aw():
    mw.withdraw()
    aw.deiconify()

def aw_to_mw():
    aw.withdraw()
    mw.deiconify()

def mw_to_vw():
    mw.withdraw()
    vw.deiconify()
    view()

def vw_to_mw():
    vw.withdraw()
    mw.deiconify()


mw = Tk()
mw.title("Main Window")
mw.geometry("600x600+300+30")
f = ("Arial", 25, "bold")

mw_btn_add = Button(mw, text="Add Student", font=f, command=mw_to_aw)
mw_btn_view = Button(mw, text="View Student", font=f, command=mw_to_vw)
mw_btn_add.pack(pady=10)
mw_btn_view.pack(pady=10)


aw = Toplevel()
aw.title("Add Student")
aw.geometry("600x600+300+30")

aw_lab_rno = Label(aw, text="Enter Roll No", font=f)
aw_ent_rno = Entry(aw, font=f, bd=3)
aw_lab_name = Label(aw, text="Enter Name", font=f)
aw_ent_name = Entry(aw, font=f, bd=3)

aw_btn_save = Button(aw, text="Save Student", font=f, command=save)
aw_btn_back = Button(aw, text="Back to Main", font=f, command=aw_to_mw)

aw_lab_rno.pack(pady=5)
aw_ent_rno.pack(pady=5)
aw_lab_name.pack(pady=5)
aw_ent_name.pack(pady=5)
aw_btn_save.pack(pady=5)
aw_btn_back.pack(pady=5)

aw.withdraw()


vw = Toplevel()
vw.title("View Student")
vw.geometry("600x600+300+30")

vw_st_data = ScrolledText(vw, font=f, width=30, height=10)
vw_btn_back = Button(vw, text="Back to Main", font=f, command=vw_to_mw)

vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)

vw.withdraw()


def quit_app():
    if askyesno("Exit", "Do you want to exit?"):
        mw.destroy()

mw.protocol("WM_DELETE_WINDOW", quit_app)
aw.protocol("WM_DELETE_WINDOW", quit_app)
vw.protocol("WM_DELETE_WINDOW", quit_app)

mw.mainloop()
