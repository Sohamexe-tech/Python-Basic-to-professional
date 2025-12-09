#wapp to read amount from user and print the final amount
#if amount is>1000--> then 10% discount, if amount is >500 then -->5% discount
#else no Discount

Amount= float(input("Enter the Amount= "))

if Amount<1:
	print("Invalid Amount")

elif Amount>1000:
	fAmount= Amount*0.9
	print("Final amount with discount is ",round(fAmount))

elif Amount>500:
	fAmount= Amount*0.95
	print("Final amount with discount is ",round(fAmount))

else:
	fAmount= Amount
	print("Final amount with discount is ",fAmount)



