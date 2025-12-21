from sqlite3 import*
con=None
try:
	con=connect("infy.db")
	sql="insert into emp values(?,?,?)"
	eid= int(input("Enter Emp id: "))
	name=input("Enter Emp name: ")
	salary=float(input("Enter Emp salary: "))
	cursor=con.cursor()
	cursor.execute(sql,(eid,name,salary))
	con.commit()
	print("record created")
	
except Exception as e:
	con.rollback()
	print("issue",e)
finally:
	if con is not None:
		con.close()