#wamdpp to read list of integers & print on screen 

num=[]

while True:
	op=int(input("1 Enter element, 2 view elements , 3 exit :- "))

	if op==1:
		ele=int(input("Enter element "))
		num.append(ele)

	elif op==2:
		print(num)

	elif op==3:
		print("bye")
		break

	else:
		print("invalid option")