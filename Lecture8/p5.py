#wapp to find first non repeatting character
#you are given a string s
#Find and return the first character that appers only once usinng a dictionary

string=input("enter a string: ")

counter={}
for s in string:
	co=counter.get(s)
	if co==None:
		counter[s]=1
	else:
		counter[s]=co+1
print(counter)

found=False
for c in counter:
	if counter[c]==1:
		print(c,counter[c])
		found=True
		break

if not found:
	print(-1)

	
	