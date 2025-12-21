#wapp to view records

from sqlite3 import*
con=None
try:
	con=connect("infy.db")
	sql="select * from emp"
	cursor=con.execute(sql)
	data=cursor.fetchall()
	for d in data:
		print(d)
except Exception as e:
	print("issue",e)
finally:
	if con is not None:
		con.close()