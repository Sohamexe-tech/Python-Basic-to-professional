#wapp to demo string functions 

s1="kamalSir"
print(s1.upper()) #co
print(s1.lower())

s2="	kamal	sir	"
print("$"+s2+"$")
print("$"+s2.strip()+"$")
print("$"+s2.lstrip()+"$")
print("$"+s2.rstrip()+"$")

s3="kamalsirclasses"
print(s3.islower())
print(s3.isupper())
print(s3.isalpha())
print(s3.isalnum())
print(s3.isdigit())
