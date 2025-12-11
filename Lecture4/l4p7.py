#wapp to print
#$
#$ $
#$ $ $
#$ $ $ $ 

from time import sleep
n=int(input("Enter the count = "))

if n>0:
	for count in range (1,n+1,1):
		print(count*"$ ")
		n+=1

else:
	print("invalid no.")
		