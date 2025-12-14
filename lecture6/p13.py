#wapp to add numbers 

numbers=[]
while True:
	op=int(input("1 enter,2 view ,3 add,4 exit "))
	if op==1:
		ele=float(input("enter element "))
		numbers.append(ele)
	elif op==2:
		print(numbers)
	
	elif op==3:
		sum=0
		for n in numbers:
			sum=sum+n
		print("sum=",sum)

	elif op==4:
		break

	else:
		print("invalid options")