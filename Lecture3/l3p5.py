#wapp to chant mantras multiple times and butify it
from time import sleep
n=int(input("Enter the number= "))

if n>0:
	count=1
	while count<=n:
		print("\n count=",count)
		sleep(0.5)
		print("*"*20)
		print("Shree Swami Samarth")
		print("*"*20)
		sleep(0.5)
		print("Ganpati Bappa Morya")
		print("*"*20)
		sleep(2)

		count=count+1

else:
	print("invalid input")