#lib for creating GUI

from tkinter import*

#to create GUI window

root=Tk()

#to customize the window
root.title("My First App")
root.geometry("600x300+500+300")

#to show the msg 
f=("Arial",50,"bold")
lab=Label(root,text="Weclome to GUI", font=f,fg="black")
lab.pack(pady=50)

#to show the window

root.mainloop()
