from tkinter import *
from tkinter.messagebox import showinfo, showerror
from pymongo import MongoClient

def db_setup():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["profile23dec25"]
        db["candidates"]
    except Exception as e:
        print("issue", e)
    finally:
        if con is not None:
            con.close()

def save():
    con = None
    try:
        name = ent_name.get().strip()
        phone = ent_phone.get().strip()

        if name == "":
            raise Exception("Name cannot be empty")

        if phone == "":
            raise Exception("Phone number cannot be empty")

        if " " in phone:
            raise Exception("Phone number cannot contain blank spaces")

        if not phone.isdigit():
            raise Exception("Phone number must contain only digits")

        if len(phone) > 10:
            raise Exception("Phone number cannot be more than 10 digits")

        phone = int(phone)

        if g.get() == 1:
            gender = "male"
        else:
            gender = "female"

        lang = ""
        if py.get() == 1:
            lang += "Python "
        if ja.get() == 1:
            lang += "Java "
        if js.get() == 1:
            lang += "JavaScript "

        con = MongoClient("localhost", 27017)
        db = con["profile23dec25"]
        coll = db["candidates"]

        document = {
            "name": name,
            "phone": phone,
            "gender": gender,
            "language": lang.strip()
        }

        coll.insert_one(document)

        showinfo("Success", "Profile Saved")

        ent_name.delete(0, END)
        ent_phone.delete(0, END)
        g.set(1)
        py.set(0)
        ja.set(0)
        js.set(0)
        btn_submit.focus()

    except Exception as e:
        ent_name.delete(0, END)
        ent_phone.delete(0, END)
        btn_submit.focus()
        showerror("Error", e)

    finally:
        if con is not None:
            con.close()

db_setup()

root = Tk()
root.title("Profile App by Soham Dalvi")
root.geometry("900x700+300+20")
root.configure(bg="honeydew2")

f = ("Arial", 30, "bold")

lab_header = Label(root, text="Profile App", font=f, bg="honeydew2")
lab_header.place(x=400, y=10)

lab_name = Label(root, text="Enter Name", font=f, bg="honeydew2")
ent_name = Entry(root, font=f)
lab_name.place(x=50, y=100)
ent_name.place(x=400, y=100)

lab_phone = Label(root, text="Enter Phone", font=f, bg="honeydew2")
ent_phone = Entry(root, font=f)
lab_phone.place(x=50, y=170)
ent_phone.place(x=400, y=170)

g = IntVar()
g.set(1)

lab_gender = Label(root, text="Gender", font=f, bg="honeydew2")
rb_male = Radiobutton(root, text="Male", font=f, variable=g, value=1, bg="honeydew2")
rb_female = Radiobutton(root, text="Female", font=f, variable=g, value=2, bg="honeydew2")
lab_gender.place(x=50, y=250)
rb_male.place(x=400, y=250)
rb_female.place(x=600, y=250)

py = IntVar()
ja = IntVar()
js = IntVar()

lab_lang = Label(root, text="Select Languages", font=f, bg="honeydew2")
cb_py = Checkbutton(root, text="Python", font=f, variable=py, bg="honeydew2")
cb_ja = Checkbutton(root, text="Java", font=f, variable=ja, bg="honeydew2")
cb_js = Checkbutton(root, text="JavaScript", font=f, variable=js, bg="honeydew2")
lab_lang.place(x=50, y=320)
cb_py.place(x=400, y=320)
cb_ja.place(x=400, y=390)
cb_js.place(x=400, y=460)

btn_submit = Button(root, text="Submit", font=f, width=15, command=save)
btn_submit.place(x=400, y=550)

root.mainloop()
