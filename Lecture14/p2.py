#wapp to create document / records

from pymongo import*
con=None
try:
	con=MongoClient("localhost",27017)
	db=con["kc23dec25"]
	coll=db["student"]

	mn=input("enter movie name: ")
	re=input("enter movie review: ")
	document={"mn":mn,"re":re}
	coll.insert_one(document)
	print("thankyou for writing the review")
	
except Ecxeption as e:
	print ("issue",e)
finally:
	if con is not None:
		con.close()
