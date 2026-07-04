# Binary Search

def binary_search(data, x):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] < x:
            low = mid + 1

        elif data[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


data = []

while True:
    op = int(input("1 enter, 2 show, 3 search and 4 exit "))

    if op == 1:
        ele = int(input("Enter element: "))
        data.append(ele)
        data.sort()

    elif op == 2:
        print(data)

    elif op == 3:
        x = int(input("Enter element to search: "))
        pos = binary_search(data, x)

        if pos == -1:
            print(x, "not found")
        else:
            print(x, "found at index", pos)

    elif op == 4:
        break

    else:
        print("Sorry, I don't understand.")