# wapp to track the email

emails=set()
while True:
	op=int(input("1 Enter, 2 View, 3 Remove ,4 Exit \n"))
	if op==1:
		em=input("enter your email ")
		emails.add(em)

	elif op==2:
		print(em)

	elif op==3:
		em=input("enter your email ")
		if em in emails:
			emails.remove(em)
		else:
			print(em,"not found")
	elif op==4:
		break
	
	else:
		print("invalid option")

