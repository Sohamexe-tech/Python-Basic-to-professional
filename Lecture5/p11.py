#wapf to check weather the function is an even no. or odd no.

def show(num):
	print("enter the no.")

def check(num):
	if num%2==0:
		print("the number is an even no.")
	
	else:
		print("the number is an odd no.")

n=float(input("enter the number= "))
show(n)
check(n)