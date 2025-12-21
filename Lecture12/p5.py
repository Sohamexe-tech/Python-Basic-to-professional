#wapp to update student record

from sqlite3 import*

con=None
try:
	con=connect("kc.db")
	sql="delete from student where rollno=?"
	rollno=int(input("Enter the roll no.: "))
	
	cursor= con.cursor()
	cursor.execute(sql,(rollno,))
	con.commit()
	if cursor.rowcount>0:\
		print(cursor.rowcount,"records deleted successfull.")
	else:
		print("no record found with roll no.", rollno)
	
except Exception as e:
	con.rollback()
	print("issue ",e)
finally:
	if con is not None:
		con.close()