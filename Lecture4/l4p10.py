from getpass import getpass 

username=getpass("Enter the username= ")
password=getpass("Enter the password= ")
if (username=="kamal") and (password=="class"):
	print("success")

else:
	print("failure")
#input()--> echo
#getpass()--> non echo

