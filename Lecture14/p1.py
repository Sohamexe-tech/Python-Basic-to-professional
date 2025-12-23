#wapp to create db and collection 

from pymongo import*
con=None
try:
	con= MongoClient("local",27017)
	db=con["kc23dec25"]
	coll=db["student"]
	print("db and coll done")
except Exception as  e:
	print("issue ",e)
finally:
	if con is not None:
		con.close()