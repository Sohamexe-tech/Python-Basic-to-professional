#wapf to return sum and avg of three numbers

def compute(n1,n2,n3):
	sum=n1+n2+n3
	avg=sum/3
	return sum,avg

num1=float(input("enter first number= "))
num2=float(input("enter secound number= "))
num3=float(input("enter third number= "))

sum,avg= compute(num1,num2,num3)
print("addition of number is= ", round(sum,2))
print("average of the number is= ",round(avg,2))
