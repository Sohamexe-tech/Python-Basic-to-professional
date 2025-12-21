# wapp  to find square of givwn number 

print("welcome")

try:
	num=float(input("enter number: "))
	sqrt=num**0.5
	print("square root =",round(sqrt,2))

except ValueError:
	print("enter correct number")
except KeyboardInterrupt:
	print("enter integer only are you in a rush")
except TypeError:
	print("enter correct number")

print("have a good day")
print("bye")