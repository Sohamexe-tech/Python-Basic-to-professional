from tkinter import*
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from pymongo import*
from datetime import*

def db_setup():
	con=None
	try:
		con=MongoClient("localhost",27017)
		db=con["kc23dec25"]
		coll=db["person"]

	except Exception as e:
		print("issue ",e)
	finally:
		if con is not None:
			con.close()

db_setup()
	
def save():
	mn=ent_name.get()
	if mn =="":
		showerror("Name issue","Movie name should not empty")
		ent_name.focus()
		return

	re=st_review.get(00.0,END)
	if re.strip()=="":
		showerror("review issue","Movie review should not empty")
		st_review.focus()
		return

	con=None
	try:
		con=MongoClient("localhost", 27017)
		db=con["kc23dec25"]
		coll=db["person"]
		
		dt=datetime.now()
		document={"movie Name":mn,"Movie Review":re,"dt":str(dt)}
		coll.insert_one(document)
		showinfo("success","thank you for the review")
		ent_name.delete(0,END)
		st_review.delete(0.0,END)
		ent_name.focus()
	except Exception as e:
		print("issue ",e)
	finally:
		if con is not None:
			con.close()

root=Tk()
root.title("Movie Review App by Soham Dalvi")
root.geometry("600x600+300+30")
f=("cambria",30,"bold")

lab_header=Label(root,text="Movie Review App",font=f)
lab_name=Label(root,text="Enter Movie Name ",font=f)
ent_name=Entry(root,bd=3,font=f)
lab_review=Label(root,text="Enter Movie Review ",font=f)
st_review=ScrolledText(root,font=f,width=20,height=4)
btn_submit=Button(root,text="Submit Review",font=f,command=save)

lab_header.pack(pady=5)
lab_name.pack(pady=5)
ent_name.pack(pady=5)
lab_review.pack(pady=5)
st_review.pack(pady=5)
btn_submit.pack(pady=5)

root.mainloop()
