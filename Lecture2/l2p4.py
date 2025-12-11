#wapp to read radius from the user and if radius is valid then print are and circumference of the circle

radius=float(input("enter the radius of the circle= "))

if radius>0.0:
	area=3.14*radius**2
	circumference=2*3.14*radius
	print("area= ", round(area,2))
	print("circumference= ",round(circumference,2))
else:
	print("invalid radius")
