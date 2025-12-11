#wapp to find sum oif first "n"+ve integers 
#i/p:5	1+2+3+4+5=15
#i/p:3	1+2+3=6

n=int(input("Enter the value of n= "))
if n>0:
	sum=0
	for i in range (1,n+1,1):
		sum=sum+i #also: sum+=i
	
	print("value= ",sum)
	



else:
	print("invalid input")