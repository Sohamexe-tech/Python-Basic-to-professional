#wapp to readlist of numbers and print the minimum and maximum 

number=[]

while True:
	op=int(input("1 Enter , 2 View , 3 Minimum , 4 Maximum , 5 Exit \n"))
	if op==1:
		ele=input("enter element= ")
		number.append(ele)
	elif op==2:
		print(ele)
	
	elif op==3:
		Minimum=min(number)
		print(Minimum)

	elif op==4:
		Maximum=max(number)
		print(Maximum)

	elif op==5:
		break

	else:
		print("invalid option")
