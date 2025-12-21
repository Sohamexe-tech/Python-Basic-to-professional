#wapp to count occurrence of each letter 
#kkammmal  {'k':2,'a':2, 'm':3, 'l':1}
#{'soham': 1, 'dalvi': 1, 'loves': 1, 'to': 1, 'read': 1, 'books': 1, 'and': 1, 'play': 1, 'guitar': 1}
counter={}
word=input("enter a word : ")

for w in word:
	co=counter.get(w)
	if co ==None:
		counter[w]=1
	else:
		counter[w]=co+1

print(counter)