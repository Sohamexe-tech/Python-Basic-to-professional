from tkinter import *
import requests
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def gm():
    url = "https://quotes-api-self.vercel.app/quote"
    response = requests.get(url)
    data = response.json()

    quote = data["quote"]
    author = data["author"]

    lab_quote.configure(text=quote)
    lab_author.configure(text=author)


root = Tk()
root.title("Motivational Quotes")
root.geometry("1100x500+300+30")
root.configure(bg="lightblue")

f = ("Times New Roman", 30, "bold")
lab_title = Label(root,text="Press The Button And Get Motivated", font=f, bg="lightblue")
btn_gm = Button(root, text="#Get Motivational Quote#", font=f, command=gm, bg="White", border=5, relief="raised")
lab_quote = Label(root, font=f, wraplength=700, border=2, relief="solid", bg="red")
lab_author = Label(root, font=f, bg="lightblue")

lab_title.pack(pady=10)
btn_gm.pack(pady=10)
lab_quote.pack(pady=10)
lab_author.pack(pady=10)

root.mainloop()
