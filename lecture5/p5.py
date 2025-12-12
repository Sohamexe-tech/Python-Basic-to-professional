#wapp to read first name and last name 
#and print welcome firstname last name
#using data validation 

fname=input("Enter first name ")
if fname=="":
	print("first name cannot be empty")
	exit()
if not fname.isalpha():
	print("first name should contain only alphabet")
	exit()

lname=input("Enter last name ")
if lname=="":
	print("last name cannot be empty")
	exit()
if not lname.isalpha():
	print("last name should contain only alphabet")
	exit()

msg="welcome "+ fname+" "+lname
print("msg=",msg)

print("welcome "+fname+" "+lname) 
