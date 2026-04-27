from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt
import numpy as np
import re

days = []
burger = []
pizza = []

def add_data():
    try:
        d = ent_day.get()
        b = ent_burger.get()
        p = ent_pizza.get()

        if d == "" or b == "" or p == "":
            showerror("Input Error", "All fields are required")
            return

        if not re.match("^[A-Za-z0-9 ]+$", d):
            showerror("Input Error", "No special symbols allowed in Day")
            return

        b = int(b)
        p = int(p)

        if b < 0 or p < 0:
            showerror("Input Error", "Negative values not allowed")
            return

        days.append(d)
        burger.append(b)
        pizza.append(p)

        lbl_status.config(text=f"Added data for {d}")

        ent_day.delete(0, END)
        ent_burger.delete(0, END)
        ent_pizza.delete(0, END)
        ent_day.focus()

    except ValueError:
        showerror("Input Error", "Sales must be numeric values")


def show_chart():
    if len(days) == 0:
        showerror("No Data", "Please add at least one entry")
        return

    x = np.arange(len(days))
    width = 0.3

    plt.figure(figsize=(10,5))
    plt.bar(x, burger, width=width, label="Burger")
    plt.bar(x + width, pizza, width=width, label="Pizza")

    plt.xticks(x + width/2, days)
    plt.xlabel("Days")
    plt.ylabel("Sales")
    plt.title("Soham's Cafe - Burger vs Pizza")
    plt.legend()

    plt.tight_layout()
    plt.show()



root = Tk()
root.title("Cafe Sales App")
root.geometry("700x700+300+30")

Label(root, text="Day",
      font=("Cambria", 18)).pack(pady=(20, 5))

ent_day = Entry(root,
                font=("Cambria", 18),
                width=25)
ent_day.pack(ipady=8)

Label(root, text="Burger Sales",
      font=("Cambria", 18)).pack(pady=(20, 5))

ent_burger = Entry(root,
                   font=("Cambria", 18),
                   width=25)
ent_burger.pack(ipady=8)

Label(root, text="Pizza Sales",
      font=("Cambria", 18)).pack(pady=(20, 5))

ent_pizza = Entry(root,
                  font=("Cambria", 18),
                  width=25)
ent_pizza.pack(ipady=8)

Button(root,
       text="Add Data",
       font=("Cambria", 16),
       width=15,
       height=1,
       command=add_data).pack(pady=20)

Button(root,
       text="Show Chart",
       font=("Cambria", 16),
       width=15,
       height=1,
       command=show_chart).pack(pady=10)

lbl_status = Label(root,
                   text="",
                   font=("Cambria", 14),
                   fg="green")
lbl_status.pack(pady=10)

root.mainloop()

