# wapp to check if the given integer 
# is even or odd 

print("welcome")

try:
	num=int(input("enter intreger: "))
	if num%2==0:
		print("integer is even")
	else:
		print("odd")
except ValueError:
	print("enter integer value only")
	
print("bye")
 