#wapp to find factorial of the numbers

n=int(input("enter the the desired number= "))

if n>=0:
	i=1
	factorial=1
	while i<=n:
		factorial=factorial*i
		i=i+1

		print("factorial= ", factorial)
else:
	print("Invalid number")
