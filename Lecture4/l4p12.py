#wapp to read name and sort the name 
#i/p: kamal aakim
#i/p: tina aint

name=input("enter name ")

#method1
res=sorted(name)
print(res)
sname="".join(res)
print(sname)

#method2
ssname="".join(sorted(name))
print(ssname)