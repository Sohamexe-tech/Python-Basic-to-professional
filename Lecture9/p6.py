#wapp to read and print content
#of an existing file

import os 
fn=input("enter filename: ")

if os.path.exists(fn):
	f=None
	try:
		f=open(fn,"r")
		data=f.read()
		print(data)
		
		
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
else:
	print(fn,"dose not exist: ")