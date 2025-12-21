#professional  way
import os
fn=input("enter filename: ")

if os.path.exists(fn):
	print(fn,"already exists")
else:
	f=None
	try:
		f=open(fn,"w")
		print(fn,"created")
	except FileNotFoundError:
		print("check directory name")
	except PermissionError:
		print("sorry no permission")
	except Exception as e:
		print("other exception",e)
	finally:
		if f is not None:
			f.close()