from pyrebase import*

firebaseConfig = {
  "apiKey": "AIzaSyCZoSneZmnRvTtPAiK45DVsiRZkxJHZJAw",
  "authDomain": "ffandsf.firebaseapp.com",
  "databaseURL": "https://ffandsf-default-rtdb.firebaseio.com",
  "projectId": "ffandsf",
  "storageBucket": "ffandsf.firebasestorage.app",
  "messagingSenderId": "1088699852908",
  "appId": "1:1088699852908:web:34138cfc280ed18467d049"
}

fb=initialize_app(firebaseConfig)
db=fb.database()

sf=input("Enter Short Form : ")
ff=input("Enter Full Form : ")
doc={"sf":sf,"ff":ff}
db.child("acronyms").push(doc)
print("Saved Successfully")