#wapp to count n to 0 and print Happy New Year 
from time import sleep
n=int(input("Enter countdown= "))

if n>=0:
	while n>=1:
		print(n)
		n=n-1
		sleep(1)
	
	print("happy New Year")
else:
	print("Invalid no.")
	
	