#wapp to check weathe the given string is a palindrome
#string which read the same L to R and R to L

string=input("enter the string ")

rstring="".join(reversed(string))

if string==rstring:
	print("yes it is a palindrome")
else:
	print("no it is a palindrome")
	