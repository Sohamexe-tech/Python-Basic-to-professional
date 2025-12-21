from  tkinter import*

root=Tk()
root.title("Even or Odd Finder")
root.geometry("700x300+300+30")
root.resizable(False,False)
f=("Times New Roman",30,"bold")

def check():
	try:
		num=int(ent_num.get())
		if num%2==0:
			msg="given no. is even"
		else:
			msg="given no. is odd"
	except ValueError:
		msg="enter correct no"
		lab_msg.configure(text=msg,fg="red")
		ent_num.focus()
		return

lab_header=Label(root,text="Even Odd Finder",font=f)
lab_header.pack(pady=10)

lab_num=Label(root,text="Enter Integer",font=f)
lab_num.pack(pady=10)

ent_num=Entry(root,font=f)
ent_num.pack(pady=10)

btn_check=Button(root,text="check",font=f, command=check)
btn_check.pack(pady=10)

lab_msg=Label(root,font=f)
lab_msg.pack(pady=10)

root.mainloop()
		