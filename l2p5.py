#wapp to read Lenght and Breath from user if they are valid the print area and perimeter of rectangle

length= float(input("enter length= "))
breadth= float(input("enter breath= "))

if(length>0) and (breadth>0) :

	area= length*breadth
	perimeter= 2*(length+breadth)
	print("area=",round(area,2))
	print("perimeter=",round(perimeter,2))
else:
	print("invalid input")

