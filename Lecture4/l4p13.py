#wapp to read two strings and check if they are anagrams 
#anagras--> two string having some letters but different meaning 
#	listen silent	heart earth	fired fried
#	eilnst eilnst	aehrt aehrt

s1=input("Enter 1st string ")
ss1name="".join(sorted(s1))

s2=input("Enter 2nd string ")
ss2name="".join(sorted(s2))

if ss1name==ss2name :
	print("they are anegrams")
else:
	print("they are not ")