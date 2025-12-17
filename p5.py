#wapp to write into an existing file 
#Old data+Naya data

import os 
fn=input("enter filename: ")

if os.path.exists(fn):
	f=None
	try:
		f=open(fn,"a")
		data= input("enter data to write ")
		f.write(data+"\n")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
else:
	print(fn,"dose not exist: ")