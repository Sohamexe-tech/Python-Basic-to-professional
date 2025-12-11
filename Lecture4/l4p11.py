#maskpass

from maskpass import askpass

username=input("Enter the username= ")
password=askpass("Enter the password= ")
if (username=="kamal") and (password=="class"):
	print("success")

else:
	print("failure")
