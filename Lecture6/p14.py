#wapp to track friends attending birthday party

friends=[]
while True:
	op=int(input("1 enter, 2 view ,3 remove, 4 exit"))
	if op==1:
		name=input("Entre your name :")
		friends.append(name)
	
	elif op==2:
		print(friends)

	elif op==3:
		name=input("enter your name")
		friends.remove(name)

	elif op==4:
		break

	else:
		print("inivalid option")