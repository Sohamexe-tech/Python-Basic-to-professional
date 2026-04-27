#wamdpp to read list of integers & print 1) positive 2) negative 3) zeros

num=[]
while True:
	op=int(input("1 Enter element, 2 view elements , 3 output,4 exit :- "))

	if op==1:
		ele=int(input("Enter element "))
		num.append(ele)

	elif op==2:
		print(num)

	elif op==3:
		pc,nc,zc=0,0,0
		for n in num:

			if n>0:
				print("no. is possitive")
				pc=pc+1
			elif n<0:
				print("no. is negative")
				nc=nc+1
			else:
				print("no. is zero")
				zc=zc+1
		print(pc,nc,zc)
				
	elif op==4:
		print("bye")
		break
	else:
		print("invalid option")

