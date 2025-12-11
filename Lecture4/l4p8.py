#wapp to print
#* * * * 
#* * *
#* * 
#* 

from time import sleep
n=int(input("Enter the count = "))

if n>0:
	for count in range (n,0,-1):
		print(count*"* ")
		n+=1

else:
	print("invalid no.")
		