from tkinter import * 
root = Tk() 
root.title("Square Root Finder App ") 
root.geometry("1000x500+300+30") 
f = ("Arial", 30, "bold") 
def find(): 
    try: 
        num = float(ent_num.get())  
        res = num ** 0.5 
        msg = "square root = " + str(round(res, 2))
        lab_msg.configure(text=msg) 

    except ValueError: 
        msg = "please enter numbers only" 
        lab_msg.configure(text=msg) 

    except TypeError: 
        msg = "please enter +ve numbers only"
        lab_msg.configure(text=msg) 
 
lab_header = Label(root, text="Square Root Finder", font=f) 
lab_header.place(x=300,y=30) 
lab_num = Label(root, text="Enter Number", font=f) 
lab_num.place(x=50, y=120) 
ent_num=Entry(root, font=f) 
ent_num.place(x=400, y=120) 
btn_find = Button(root, text="Find Square Root ", font=f, command=find) 
btn_find.place(x=400, y=220) 
lab_msg = Label(root, font=f) 
lab_msg.place(x=200, y=350) 
root.mainloop()