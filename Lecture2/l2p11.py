# Match case Statement 

Rating=float(input("Enater rating between 1 to 5= "))

match Rating:

	case	5:	print("Excellent")
	case	4:	print("Excellent")	
	case	3:	print("Ok")
	case	2:	print("OK")
	case	1:	print("Poor")
	case	_:	print("Invalid")
