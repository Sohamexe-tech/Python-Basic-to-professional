#wapp to view student records

from sqlite3 import*

con=None
try:
	con=connect("kc.db")
	sql="select * from student"
	cursor= con.cursor()
	cursor.execute(sql)
	data=cursor.fetchall()
	for d in data:
		print("rollno= ",d[0],"name= ",d[1],"marks= ",d[2])
except Exception as e:
	print("issue ",e)
finally:
	if con is not None:
		con.close()
	