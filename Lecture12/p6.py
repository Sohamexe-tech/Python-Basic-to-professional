from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *

def db_setup():
    con = None
    try:
        con = connect("winner.db")
        # Corrected syntax: IF NOT EXISTS
        sql = "CREATE TABLE IF NOT EXISTS student(name TEXT, college TEXT, title TEXT)"
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print("Setup issue:", e)
    finally:
        if con is not None:
            con.close()

db_setup()

def save():
    name = ent_name.get().strip()
    college = ent_college.get().strip()
    title = ent_title.get().strip()

    # Validation
    if name == "":
        showerror("Name issue", "Name should not be empty")
        ent_name.focus()
        return
    if college == "":
        showerror("College issue", "College should not be empty")
        ent_college.focus()
        return
    if title == "":
        showerror("Title issue", "Title should not be empty")
        ent_title.focus()
        return

    # Database Insertion (Now inside the save function)
    con = None
    try:
        con = connect("winner.db")
        sql = "INSERT INTO student VALUES (?, ?, ?)"
        cursor = con.cursor()
        cursor.execute(sql, (name, college, title))
        con.commit()
        
        showinfo("Success", "Record saved successfully!")
        
        # Clear fields
        ent_name.delete(0, END)
        ent_college.delete(0, END)
        ent_title.delete(0, END)
        ent_name.focus()
        
    except Exception as e:
        if con: con.rollback()
        showerror("Database Issue", str(e))
    finally:
        if con is not None:
            con.close()

# --- UI Setup ---
root = Tk()
root.title("SIH Winners")
root.geometry("600x650+300+60")
f = ("Times New Roman", 18) # Added font size for better visibility

lab_header = Label(root, text="SIH Winner Registration", font=("Times New Roman", 24, "bold"))
lab_header.pack(pady=20)

lab_name = Label(root, text="Enter Student Name", font=f)
lab_name.pack()
ent_name = Entry(root, font=f)
ent_name.pack(pady=5)

lab_college = Label(root, text="Enter College Name", font=f)
lab_college.pack()
ent_college = Entry(root, font=f)
ent_college.pack(pady=5)

lab_title = Label(root, text="Enter Project Title", font=f)
lab_title.pack()
ent_title = Entry(root, font=f)
ent_title.pack(pady=5)

btn_submit = Button(root, text="Submit Record", font=f, command=save, bg="lightblue")
btn_submit.pack(pady=30)

root.mainloop()