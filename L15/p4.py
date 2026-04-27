from tkinter import *
from tkinter.messagebox import *
from pyrebase import *

firebaseConfig = {
    "apiKey": "AIzaSyCZoSneZmnRvTtPAiK45DVsiRZkxJHZJAw",
    "authDomain": "ffandsf.firebaseapp.com",
    "databaseURL": "https://ffandsf-default-rtdb.firebaseio.com",
    "projectId": "ffandsf",
    "storageBucket": "ffandsf.firebasestorage.app",
    "messagingSenderId": "1088699852908",
    "appId": "1:1088699852908:web:34138cfc280ed18467d049"
}

try:
    fb = initialize_app(firebaseConfig)
    db = fb.database()
except Exception as e:
    showerror("Firebase Error", e)

def clear_focus():
    ent_sf.delete(0, END)
    ent_sf.focus()

def find():
    try:
        sf = ent_sf.get()

        # Empty check
        if sf == "":
            showerror("Error", "Short Form cannot be empty")
            clear_focus()
            lab_msg.config(text="")
            return

        # Space check
        if " " in sf:
            showerror("Error", "Spaces are not allowed")
            clear_focus()
            lab_msg.config(text="")
            return

        # Numeric check
        if sf.isdigit():
            showerror("Error", "Numbers are not allowed")
            clear_focus()
            lab_msg.config(text="")
            return

        # Special symbol check
        if not sf.isalpha():
            showerror("Error", "Special symbols are not allowed")
            clear_focus()
            lab_msg.config(text="")
            return

        sf = sf.upper()

        existing = db.child("acronyms").order_by_child("sf").equal_to(sf).get()
        data = existing.val()

        if data:
            for k, v in data.items():
                lab_msg.config(text=v["ff"])
        else:
            lab_msg.config(text="Not Found")

        # Clear & focus after execution
        clear_focus()

    except Exception as e:
        showerror("Error", f"Something went wrong\n{e}")
        clear_focus()
        lab_msg.config(text="")

root = Tk()
root.title("Whats The Full Form?")
root.geometry("700x500+300+30")
f = ("Times New Roman", 30, "bold")

lab_header = Label(root, text="Whats The Full Form?", font=f)
lab_sf = Label(root, text="Enter Short Form : ", font=f)
ent_sf = Entry(root, bd=3, font=f)
btn_find = Button(root, text="Find Full Form", font=f, command=find)
lab_msg = Label(root, text="", font=f)

lab_header.pack(pady=5)
lab_sf.pack(pady=5)
ent_sf.pack(pady=5)
btn_find.pack(pady=5)
lab_msg.pack(pady=5)

ent_sf.focus()   # Initial focus

root.mainloop()
