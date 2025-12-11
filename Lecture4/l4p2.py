#wapp to chant mantras "n" times 

from time import sleep 
n=int(input("Enter the value of n "))

if n>0:
	for count in range (1,n+1,1):
		print("count=",count)
		sleep(0.5)
		print("shree swami samarth")
		sleep(0.5)
		print("Ganpati Bappa Morya")
		print("*"*30)
		sleep(2)


else:
	print("invalid input")