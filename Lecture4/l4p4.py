#wapp to find factorial of first "n"+ve integers 
#i/p:5	1*2*3*4*5=
#i/p:3	1*2*3=

n=int(input("Enter the value of n= "))
if n>0:
	factorial=1
	for i in range (1,n+1,1):
		factorial=factorial*i #also: factorial*=i
	
	print("factorial= ",factorial)
	



else:
	print("invalid input")