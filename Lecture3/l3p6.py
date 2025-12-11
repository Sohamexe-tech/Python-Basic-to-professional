# wapp to find sum of first "n" +ve integers 
#Ex:- i/p:5 1+2+3+4+5=15

n=int(input("Enter the Number= "))

if n>0:
	i=1
	sum=0

	while i<=n:
		sum=sum+i
		i=i+1

	print("sum=",sum)

else:
	print("Invalid input")