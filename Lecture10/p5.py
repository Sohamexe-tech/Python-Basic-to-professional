from tkinter import*
from datetime import*

root=Tk()
root.title("Greeting App ")
root.geometry("700x500+300+30")
root.resizable(False,False)
f=("Times New Roman",30,"bold")

def show():
	name=ent_name.get()

	if name=="":
		msg="Please Enter Name"
		lab_msg.configure(text=msg,fg="red")
		ent_name.focus()
		return
		
	if name.strip()=="":
		msg="name should not be blank spaces"
		lab_msg.configure(text=msg,fg="red")
		ent_name.delete(0,END)
		ent_name.focus()
		return

	if not name.isalpha():
		msg="name should contain only alphabets"
		lab_msg.configure(text=msg,fg="red")
		ent_name.delete(0,END)
		ent_name.focus()
		return

	dt=datetime.now()
	hr=dt.hour
	if hr<12:
		msg="Good Morning "+str(name)
	elif hr<16:
		msg="Good Afternoon "+str(name)
	else:
		msg="Good Eveaning "+str(name)

	lab_msg.configure(text=msg,fg="Blue")


lab_header = Label(root,text="Greeting App",font=f)
lab_header.pack(pady=20)

lab_name = Label(root,text="Enter name",font=f)
lab_name.pack(pady=20)

ent_name = Entry(root,font=f)
ent_name.pack(pady=10)

btn_submit = Button(root,text="Submit",font=f,command=show)
btn_submit.pack(pady=10)

lab_msg = Label(root,font=f)
lab_msg.pack(pady=20)

root.mainloop()


	
