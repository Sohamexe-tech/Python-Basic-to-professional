#wapp to pprint table 

n=int(input("Enter the desired number= "))

if n>0:
	i=1
	while i<=10:
		Ans=n*i
		print(n,"x",i,"=",Ans)
		i=i+1

else:
	print("Invalid number")