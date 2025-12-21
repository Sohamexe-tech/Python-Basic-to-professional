from tkinter import*
from datetime import*

root=Tk()
root.title("Greeting App by Soham Dalvi")
root.geometry("1000x500+300+300")

dt=datetime.now()
hr=dt.hour
if hr<12:
	msg="Good Morning"
elif hr<16:
	msg="Good Afternoon"
else:
	msg="Good Eveaning"

f=("Time New Romen",50,"bold","italic")
lab=Label(root,text=msg,font=f,fg="black")
lab.pack(pady=50)

root.mainloop()
