#Selection Sort

def selection_sort(data):
	n=len(data)
	for i in range(n):
		min_index=i
		for j in range(i+1,n):
			if data[j]<data[min_index]:
				min_index=j

		data[i],data[min_index] = data[min_index],data[i]
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
		selection_sort(data)
	elif op==4:
		break
	else:
		print("Incorrect Input")