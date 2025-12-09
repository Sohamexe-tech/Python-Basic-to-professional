# Match case Statement and make it smaller

Rating=float(input("Enater rating between 1 to 5= "))

match Rating:

	case	5 | 4:	print("Excellent")	
	case	3 | 2:	print("Ok")
	case	1:	print("Poor")
	case	_:	print("Invalid")