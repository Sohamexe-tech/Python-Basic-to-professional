#wapf to print sum and avg of three numbers

def compute(n1,n2,n3):
	sum=n1+n2+n3
	avg=sum/3
	print("addition of no.is ", sum)
	print("average of the no,. is ", avg)

num1=float(input("enter first number "))
num2=float(input("enter secound number "))
num3=float(input("enter third number "))

compute(num1,num2,num3)
