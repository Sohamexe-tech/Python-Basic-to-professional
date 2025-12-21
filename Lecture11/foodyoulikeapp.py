from tkinter import*

root=Tk()
root.title("food You Like App")
root.geometry("1000x650+300+30")
f=("Caliber",30,"bold")

#event handeling
def show():
	try:
		name=ent_name.get()
		msg="Hello "+name+"! You like "+choice+" food."
		lab_msg.configure(text=msg)
	except ValueError :
		msg="Please enter valid data"
		lab_msg.configure(text=msg,fg="red")	
		ent_name.focus()
	except Exception as e:
		msg="Error: "+str(e)
		lab_msg.configure(text=msg,fg="red")
		ent_name.focus()

	name=ent_name.get()
	choice=""
	if c.get()==1:
		choice="North Indian"
	elif c.get()==2:
		choice="South Indian"
	elif c.get()==3:
		choice="Fast Food"
	msg="Hello "+name+"! You like "+choice+" food."
	lab_msg.configure(text=msg)

#user interface 
lab_heading=Label(root,text="food You Like App",font=f)
lab_heading.place(x=300,y=10)

lab_name=Label(root,text="Enter your name:",font=f)
lab_name.place(x=50,y=100)
ent_name=Entry(root,bd=2,font=f)
ent_name.place(x=400,y=100)

c=IntVar()
c.set(2)
lab_select=Label(root,text="Select your favorite food type:",font=f)
rb_ni=Radiobutton(root,text="North Indian",font=f,variable=c,value=1)
rb_si=Radiobutton(root,text="South Indian",font=f,variable=c,value=2)
rb_ff=Radiobutton(root,text="Fast Food",font=f,variable=c,value=3)
lab_select.place(x=50,y=200)
rb_ni.place(x=400,y=200)
rb_si.place(x=400,y=270)
rb_ff.place(x=400,y=340)

btn_submit=Button(root,text="Submit",font=f,command=show)
lab_msg=Label(root,text="",font=f)
btn_submit.place(x=400,y=400)
lab_msg.place(x=200,y=500)

ent_name.focus()

root.mainloop()