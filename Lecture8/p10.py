# wapp to perform ans=a/b where a&b are integers
try:
	A=int(input("enter the value of A: "))

except ValueError:
	print("enter correct number A")


try:
	B=int(input("enter the value of B: "))

except ValueError:
	print("enter correct number B")

try:
	ans=A/B
	print("The Answer is : ",ans)
except (ValueError,TypeError,ZeroDivisionError,NameError):
	print("B should not be zero")




print("bye")
