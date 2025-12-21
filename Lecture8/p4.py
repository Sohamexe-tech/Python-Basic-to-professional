#wapp to count occurence of each word in a given string 
#soham dalvi loves to read books and play guitar

counter={}
sentence=input("enter the string: ")

words=sentence.split(" ")

for w in words:
	co=counter.get(w)
	if co==None:
		counter[w]=1
	else:
		counter[w]=co+1
print(counter)