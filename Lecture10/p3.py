from datetime import*

dt=datetime.now()
print(dt)

hr=dt.hour 

if hr<12:
	print("Good Morning")
elif hr<16:
	print("Good Afternoon")
else :
	print("Good Eveaning")

