#wapp to create documents and records
#add dt

from pymongo import *
from datetime import * 

con=None
con=None
try:
	con=MongoClient("localhost", 27017)
	db=con["kc23dec25"]
	coll=db["student"]
	
	mn=input("enter movie name: ")
	re=input("enter movire review: ")
	dt=datetime.now()
	document={"mn":mn, "re":re, "dt":str(dt)}
	coll.insert_one(document)
	print("thanku for witing review")

except Exception as e:
	print("issue", e)
finally:
	if con is not None:
		con.close()