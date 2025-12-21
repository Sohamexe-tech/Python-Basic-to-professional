from sqlite3 import*
con=None

try:
	con=connect("infy.db")
	sql="create table if not exists emp(eid int primay key , name text, salary real)"
	cursor=con.cursor()
	cursor.execute(sql)
	con.commit()
	print("DB and TB done")
except Exception as e:
	con.rollback()
	print("issue", e)
finally:
	if con is not None:
		con.close()
