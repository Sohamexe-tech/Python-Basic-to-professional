#sapp to create a new file
#if the file does not exist
#Student approch

import os
fn=input("enter filename: ")

if os.path.exists(fn):
	print(fn,"Already exixts")
else:
	f=open(fn,"w")
	print(fn,"created")
	f.close ()