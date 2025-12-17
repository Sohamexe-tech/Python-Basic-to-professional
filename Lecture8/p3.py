#wapp to delete an existing file

import os

fn=input("enter filename: ")
if os.path.exists(fn):
	
	try:
		os.remove(fn)
		print(fn,"deleted")
	except Exception as e:
		print("issue",e)
else:
	
	print(fn,"Does not exist")
