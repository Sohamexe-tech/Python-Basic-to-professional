#wapf to return addition of two numbers

def add(n1,n2):
	res=n1+n2
	return res

num1=float(input("enter the first number "))
num2=float(input("enter the second number "))
res=add(num1,num2)
print("res=",res)