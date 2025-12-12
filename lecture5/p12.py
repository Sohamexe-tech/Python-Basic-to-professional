#waf to print area and circumference of a circle 

def show(radius):
	print(radius)

def area(radius):
	ans=3.14*radius**2
	print("area = ",ans)

def circumference(radius):
	ans=2*3.14*radius
	print("circumference = ",ans)

r=float(input("Enter the radius= "))

if r>0:

	show(r)
	area(r)
	circumference(r)
else:
	print("invalid input")