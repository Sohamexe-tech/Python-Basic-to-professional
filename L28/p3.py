#Insertion Sort


def insertion_sort(data):
	n = len(data)
	for i in range(1, n):
		key = data[i]
		j = i - 1
		while j >= 0 and key < data[j]:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = key
		print(data)
        


data = []
while True:
	op = int(input(" 1 Enter , 2 Show , 3 Sort , 4 Exit "))
	if op == 1:
		ele = int(input("Enter Element:"))
		data.append(ele)
	elif op == 2:
		print(data)
	elif op == 3:
		insertion_sort(data)
	elif op == 4:
		break
	else:
		print("Incorrect Input")