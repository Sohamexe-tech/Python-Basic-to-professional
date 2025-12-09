#wapp in order to know weather the year is a leap year of or not

Year=int(input("Enter year ="))

if Year%4==0:
	print(Year," Is a Leap Year")
else:
	print(Year," Is not a leap Year")