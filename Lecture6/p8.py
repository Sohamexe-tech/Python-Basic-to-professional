#DRY

n=int(input("enter value for n "))
r=int(input("enter value for r "))

def fact(num):
	f=1
	for i in range(1,n+1,1):
		f=f*i
	return f
ans=fact(n)/(fact(r)*fact(n-r))
print("ans",ans)
	



