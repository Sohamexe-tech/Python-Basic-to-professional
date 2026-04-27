from tkinter import*
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from pyrebase import*

firebaseConfig = {
  "apiKey": "AIzaSyAN-kQFaacWMmGcXernuxpm0588RR3Tnuo",
  "authDomain": "soham24dec25.firebaseapp.com",
  "databaseURL": "https://soham24dec25-default-rtdb.firebaseio.com",
  "projectId": "soham24dec25",
  "storageBucket": "soham24dec25.firebasestorage.app",
  "messagingSenderId": "626984247888",
  "appId": "1:626984247888:web:80e3fff5e1a2e2f333e755"
}

fb=initialize_app(firebaseConfig)
db=fb.database()

def save():
    name = ent_name.get().strip()

    
    if name == "":
        showerror("Name Issue", "Food name should not be empty")
        ent_name.focus()
        return

    if not all(ch.isalnum() or ch.isspace() for ch in name):
        showerror("Name Issue", "Food name can contain only letters, numbers and spaces")
        ent_name.focus()
        return

    review = st_review.get(0.0, END).strip()

    
    if review == "":
        showerror("Review Issue", "Review should not be empty")
        st_review.focus()
        return

    
    if len(review) < 5:
        showerror("Review Issue", "Review should be at least 5 characters long")
        st_review.focus()
        return

    try:
        doc = {
            "food": name,
            "review": review
        }
        db.child("review").push(doc)

        showinfo("Saved", "Thanks for the review")

        ent_name.delete(0, END)
        st_review.delete(0.0, END)
        ent_name.focus()

    except Exception as e:
        showerror("Firebase Error", str(e))
        
root=Tk()
root.title("Food Review App by Soham Dalvi")
root.geometry("600x600+300+30")
root.resizable(False,False)
f=("Times New Roman",30,"bold")

lab_header=Label(root,text="Food Review App",font=f)
lab_name=Label(root,text="Enter Food Name ",font=f)
ent_name=Entry(root,bd=3,font=f)
lab_review=Label(root,text="Enter Food Review",font=f)
st_review=ScrolledText(root,font=f,width=20,height=4)
btn_submit=Button(root,text="Submit",font=f,command=save)

lab_header.pack(pady=5)
lab_name.pack(pady=5)
ent_name.pack(pady=5)
lab_review.pack(pady=5)
st_review.pack(pady=5)
btn_submit.pack(pady=5)

root.mainloop()
		