import os 
from datetime import datetime

while True:
	op=int(input("1 Crete file, 2 read file , 3 update file , 4 exit \n"))
	if op==1:
		name=input("enter patients name: ")
		name=name+".txt"
		if os.path.exists(name):
			print(name,"Created")
		else:
			f=None
			try:
				f=open(name,"w")
				print(name,"created")
			except Exception as e:
				print("issue",e)
			finally:
				if f is not None:
					f.close()

	elif op==2:
		
			f=None
			try:
				name=input("enter patients name: ")
				name=name+".txt"
				if os.path.exists(name):
					f=open(name,"r")
					data=f.read()
					print(data)
		
		
		
			except Exception as e:
				print("issue",e)
			finally:
				if f is not None:
					f.close()

	elif op==3:
		name=input("enter patient's name: ")
		name=name+".txt"
		if os.path.exists(name):
			f=None
			try:
				f=open(name,"a")
				symptoms=input("enter symptoms: ")
				medication=input("enter Medication: ")
				dt=datetime.now()
				f.write("dt="+str(dt)+"\n")
				f.write("*"*30)
				f.write("symptoms: " +symptoms+ "\n")
				f.write("Meditation: "+medication+ "\n")
				f.write("*"*30)
				f.write("\n")
			except Exception as e:
				print("issue",e)
			finally:
				if f is not None:
					f.close()
		else:
			print(name,"dose not exist")
	
	elif op==4:
		break
	else:
		print("invalid option")
