#wapp to find square of given number 
print("good morning")

try:
	num=float(input("Enter number: "))
	square=num**2
	print("Square= ",round(square,2))

except ValueError:
	print("enter correct number")
except KeyboardInterrupt:
	print("are you in a rush")

print("have a good day")