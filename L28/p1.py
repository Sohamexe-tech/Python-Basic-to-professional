#Bubble Sort

def bubble_sort(data):
	n=len(data)
	for i in range(n):
		for j in range(0,n-i-1):
			if data[j]>data[j+1]:
				data[j],data[j+1]=data[j+1],data[j]
				print(data)

data=[]
while True:
	op=int(input(" 1 Enter , 2 Show , 3 Sort , 4 Exit "))
	if op ==1:
		ele = int(input("Enter Element:"))
		data.append(ele)
	elif op==2:
		print(data)
	elif op==3:
		bubble_sort(data)
	elif op==4:
		break
	else:
		print("Incorrect Input")