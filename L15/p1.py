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

Food=input("Enter Food Name: ")
Review=input("Enter Food Review: ")
doc={"food":Food,"review":Review}
db.child("review").push(doc)
print("Thank You For The Review")