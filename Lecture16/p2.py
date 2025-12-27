from tkinter import *
from tkinter.messagebox import *
import requests

def convert():
    try:
        val = ent_amt.get().strip()

        
        if val == "":
            raise ValueError("empty")
            

        if any(ch.isalpha() for ch in val):
            raise ValueError("alphabet")
            

       
        for ch in val:
            if not (ch.isdigit() or ch == "."):
                raise ValueError("special")
               

        aid = float(val)

        url = "https://api.exchangerate-api.com/v4/latest/USD"
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
            DOLLAR = data["rates"]["INR"]
            air = DOLLAR * aid
            msg = "₹" + str(round(air, 2))
            lab_msg.configure(text=msg, fg="blue")
        else:
            lab_msg.configure(text="Some Issue", fg="red")

    except ValueError as e:
        if str(e) == "empty":
            lab_msg.configure(text="Amount cannot be empty", fg="red")
            ent_amt.focus_set()
        elif str(e) == "alphabet":
            lab_msg.configure(text="Alphabets are not allowed", fg="red")
            ent_amt.focus_set()
        elif str(e) == "special":
            lab_msg.configure(text="Special symbols are not allowed", fg="red")
            ent_amt.focus_set()
        else:
            lab_msg.configure(text="Please enter a valid number", fg="red")
            ent_amt.focus_set()

    except Exception:
        lab_msg.configure(text="Something went wrong", fg="red")


root = Tk()
root.title("Live Dollar to INR Converter By Soham Dalvi")
root.geometry("700x400+300+30")
root.resizable(False, False)

f = ("Times New Roman", 30, "bold")

lab_header = Label(root, text="Live Currency Converter", font=f)
lab_amt = Label(root, text="Enter Amount in $:", font=f)
ent_amt = Entry(root, bd=3, font=f)
btn_convert = Button(root, text="Convert to INR", font=f, command=convert)
lab_msg = Label(root, text="", font=f)

lab_header.pack(pady=5)
lab_amt.pack(pady=5)
ent_amt.pack(pady=5)
btn_convert.pack(pady=5)
lab_msg.pack(pady=5)

root.mainloop()
