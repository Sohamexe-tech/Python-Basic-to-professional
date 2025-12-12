#waf to print are and perimeter of rectangle 

def show(l,b):
	print("length= ",l,"breadth=",b)

def area(l,b):
	ans=l*b
	print("area = ",ans)

def perimeter(l,b):
	ans=2*(l+b)
	print("perimeter = ",ans)

l=float(input("Enter the length= "))
b=float(input("Enter the breadth= "))

if (l>0) and (b>0):
	show(l,b)
	area(l,b)
	perimeter(l,b)
else:
	print("Invalid input")


