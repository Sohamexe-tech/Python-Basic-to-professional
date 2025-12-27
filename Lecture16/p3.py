from tkinter import *
from tkinter.messagebox import *
import requests

def convert():
    try:
        amt = float(ent_amt.get())
        if amt < 0:
            raise ValueError("Negative amount")
        
    except ValueError:
        showerror("Error", "Please enter a valid number")
        return
    
    except Exception as e:
        showerror("Error", "Please enter a valid number")
        return
    
    try:
        amt = float(ent_amt.get())
    except ValueError:
        showerror("Error", "Please enter a valid number")
        return

    if c.get() == 1:
        curr = "USD"
    elif c.get() == 2:
        curr = "EUR"
    else:
        curr = "GBP"

    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    data = response.json()

    rate = data["rates"][curr]
    famt = amt * rate

    msg = f"{amt} INR = {round(famt,2)} {curr}"
    lab_msg.config(text=msg)


root = Tk()
root.title("Currency Converter By Soham Dalvi")
root.geometry("1000x600+300+30")

f = ("Times New Roman", 25, "bold")

lab_header = Label(root, text="Currency Converter App (v3)", font=f)
lab_amt = Label(root, text="Enter Amount in INR", font=f)
ent_amt = Entry(root, font=f)

c = IntVar()
c.set(1)

lab_select = Label(root, text="Select Currency", font=f)
rb_usd = Radiobutton(root, text="USD", font=f, variable=c, value=1)
rb_eur = Radiobutton(root, text="EUR", font=f, variable=c, value=2)
rb_gbp = Radiobutton(root, text="GBP", font=f, variable=c, value=3)

btn_submit = Button(root, text="Convert", font=f, command=convert)
lab_msg = Label(root, font=f, fg="blue")

lab_header.place(x=250, y=20)
lab_amt.place(x=50, y=120)
ent_amt.place(x=400, y=120)

lab_select.place(x=50, y=220)
rb_usd.place(x=400, y=220)
rb_eur.place(x=550, y=220)
rb_gbp.place(x=700, y=220)

btn_submit.place(x=400, y=320)
lab_msg.place(x=200, y=420)

root.mainloop()
