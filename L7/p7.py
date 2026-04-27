#wapp to check weather to country is a part of G7 

G7=("usa","uk","canada","france","germany","italy","japan")

name=input("enter country name: ").lower()

if name in G7:
	print("Yes")
else:
	print("No")