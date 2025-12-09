#wapp to raedc marks between 0 to 100 and print A if marks >80 , B if marks>60 , C if marks > 40 else D .

Marks=int(input("Enter Marks between 0 to 100 ="))

if Marks<0:
	print("Invalid Marks ")

elif Marks>100:
	print("Invalid Marks ")

elif Marks>80:
	print("Grade A ")

elif Marks>60:
	print("Grade B ")

elif Marks>40:
	print("Grade C ")

else :
	print("Grade D ")



