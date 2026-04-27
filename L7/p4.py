# wapp to track friends attend birthday party 

friends=[]
while True:
	op=int(input("1 Enter, 2 View, 3 Remove and 4 Exit \n"))
	if op==1:
		name=input("enter the name= ")
		friends.append(name)

	elif op==2:
		print(friends)

	elif op==3:
		name=input("enter the name= ")
		if name in friends:
			friends.remove(friends)
		else:
			print("Name not found")
	elif op==4:
		break
	else:
		print("invalid option")


