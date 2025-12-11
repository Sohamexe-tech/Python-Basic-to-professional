#wapp to print table of the given no.

n=int(input("Enter the no. = "))

if n>0:
	for i in range (1,11,1):

		ans=n*i
		
		print(n,"x",i,"=",ans)
		i+=1

else:
	print("invalid no.")
		