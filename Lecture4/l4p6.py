#wapp to wish happy new year 

from time import sleep
n=int(input("Enter the count down starting = "))

if n>0:
	for count in range (n,0,-1):
		print(count)
		sleep(1)
	print("||Happy New Year||")

else:
	print("invalid no.")
		