#wapp to read length and breadth from user print area and perimeter of rectangle

length=float(input("enter length of rectangle="))
Breadth=float(input("enter Breadth of rectangle="))

Area= length*Breadth
perimeter= 2*(length+Breadth)

print("Area of Rectangle",round(Area,2))
print("Perimeter of Rectangle ",round(perimeter,2))
