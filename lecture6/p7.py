#wapp to find combination-->n!/(r!*(n-r)!)
#DIY

n=int(input("enter value for n "))
r=int(input("enter value for r "))

f1=1
for i in range(1,n+1,1):
	f1=f1*i

f2=1
for i in range(1,r+1,1):
	f2=f2*i

f3=1
for i in range(1,n-r+1,1):
	f3=f3*i

ans=f1/(f2*f3)
print("ans",ans)


