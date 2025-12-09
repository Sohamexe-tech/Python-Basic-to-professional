#wapp in order to know weather the year is a leap year of or not using match case .

Year=int(input("Enter Year= "))

match Year%4:
	case	0: print("it is a leap Year")
	case	_: print("it is not a leap Year")


