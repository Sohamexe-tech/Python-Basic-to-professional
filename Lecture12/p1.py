#wapp to create a database and table -->-->KC--> table-->student

from sqlite3 import*

con=None
try:
	con=connect("kc.db")
	sql="create table if not exists student(rollno int primary key,name text, marks int)"
	cursor=con.cursor()
	cursor.execute(sql)
	con.commit()
	print("database and table done")
except Exception as e:
		con.rollback()
		print("issue",e)
finally:
	if con is not None:
		con.close()

