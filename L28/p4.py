# linear search

def linear_search(data,x):
	for i in range(len(data)):
		if data[i]==x:
			return i
	return-1

data = []

while True:
    op = int(input("1 enter, 2 show, 3 search and 4 exit "))

    if op == 1:
        ele = int(input("Enter element: "))
        data.append(ele)

    elif op == 2:
        print(data)

    elif op == 3:
        x = int(input("Enter element to search: "))
        pos = linear_search(data, x)

        if pos == -1:
            print(x, "not found")
        else:
            print(x, "found at index", pos)

    elif op == 4:
        break

    else:
        print("Invalid Input")
