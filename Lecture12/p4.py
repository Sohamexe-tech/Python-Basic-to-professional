#wapp to update student record

from sqlite3 import*

con=None
try:
	con=connect("kc.db")
	sql="update student set name=?,marks=? where rollno=?"
	rollno=int(input("Enter the roll no.: "))
	name=input("Enter name : ")
	marks=int(input("enter marks: "))
	cursor= con.cursor()
	cursor.execute(sql,(name,marks,rollno))
	con.commit()
	print(cursor.rowcount,"record updated")
except Exception as e:
	con.rollback()
	print("issue ",e)
finally:
	if con is not None:
		con.close()