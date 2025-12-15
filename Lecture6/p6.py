#wapf to return are and perimeter of rectangle

def compute (length,breadth):
	area=length*breadth
	perimeter=2*(length+breadth)
	return area,perimeter

length=float(input("enter length "))
breadth=float(input("enter breadth "))

if(length>0)and(breadth>0):
	area,peri=compute(length,breadth)
	print ("area is = ",round(area,2))
	print ("perimeter is = ",round(peri,2))
else:
	print("invalid input")

