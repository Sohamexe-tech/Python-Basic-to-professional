#wapp to create student record

from sqlite3 import*

con=None
try:
	con=connect("kc.db")
	sql="insert into student values(?,?,?)"
	rollno=int(input("Enter the roll no.: "))
	name=input("Enter name : ")
	marks=int(input("enter marks: "))
	cursor= con.cursor()
	cursor.execute(sql,(rollno,name,marks))
	con.commit()
	print("Record Created")
except Exception as e:
	con.rollback()
	print("issue ",e)
finally:
	if con is not None:
		con.close()