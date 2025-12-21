#wapp to read roll no., fname, lname and 
#marks (0 to 100) and print on the screen 

print("welcome")

try:
	Rollno=int(input("enter rollno."))
except ValueError:
	print("Roll no. should be integer only")
	exit()
except KeyboardInterrupt:
	print("You did not enter Rollno.")
	exit()

if Rollno<1:
	print("roll no. should be minimum 1")
	exit()

fname=input("enter first name")
if fname=="":
	print("fname should not be blank spaces")
	exit()

if fname.strip()=="":
	print("fname should not be empty  space")
	exit() 

if not fname.isalpha():
	print("fanme should contain only alphabets")
	exit()

lname=input("enter last name")
if lname=="":
	print("lname should not be blank spaces")
	exit()

if lname.strip()=="":
	print("lname should not be empty  space")
	exit() 

if not lname.isalpha():
	print("lname should contain only alphabets")
	exit()

try:
	marks=int(input("Enter marks between 0 to 100: "))
except ValueError:
	print("marks Should be between 0 to 100")
	exit()


print(Rollno,fname,lname, marks)
print("bye")
