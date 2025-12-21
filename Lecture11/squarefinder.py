from tkinter import *

#creating GUI window
root = Tk()
root.title("Square Finder App")
root.geometry("700x500+300+30")
root.resizable("False", "False")
f=("Times New Roman", 30, "bold")

#event handling
def find():
    try:
        num=float(ent_num.get())
        square=num**2
        msg="Square of"+str(num)+" is "+str(round(square,2))
        lab_msg.configure(text=msg, fg="green")
    except ValueError:
        msg="Please enter numbers only"
        lab_msg.configure(text=msg, fg="red")
        ent_num.delete(0, END)
        ent_num.focus()
    except Exception as e:
        msg="Error: "+str(e)
        lab_msg.configure(text=msg, fg="red")
        ent_num.delete(0, END)
        ent_num.focus()

        #user interface components
lab_heading=Label(root, text="Square Finder", font=f, fg="blue")
lab_heading.pack(pady=20)
lab_num=Label(root, text="Enter a number:", font=f)
lab_num.pack(pady=10)
ent_num=Entry(root,bd=2,font=f)
ent_num.pack(pady=10)
btn_find=Button(root, text="Find Square", font=f, command=find)
btn_find.pack(pady=10)
lab_msg=Label(root, text="", font=f)
lab_msg.pack(pady=10)
ent_num.focus()

root.mainloop()