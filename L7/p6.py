#set operations

ODI={"amit","Virat","Dhoni"}
test={"amit","rahul","raju","soham"}

#print all name 	union

r1=ODI | test
print(r1)

r2=ODI.union(test)
print(r2)

#print common name 	intersection

r3=ODI.intersection(test)
r4=ODI&test;
print(r3)
print(r4)

#print oneday not test  difference

r5=ODI.difference(test)
r6=ODI-test;
print(r5)
print(r6)



#print oneday not test  difference

r7=test.difference(ODI)
r8=test-ODI;
print(r7)
print(r8)




