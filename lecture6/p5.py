# wapf to print aera and circumference of circle 

def compute(radius):
	area=3.14*r**2
	circumference=2*3.14*r
	print("area of the circle is= ",round(area,2))
	print("circumference of the circle is= ",round(circumference,2))

r=float(input("Enter the radius of the circle= "))

if r>0:
	compute(r)
else:
	print("Invalid input")
