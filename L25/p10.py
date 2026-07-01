class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, ele):
        if self.head is None:
            self.head = Node(ele)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = Node(ele)

    def show(self):
        print("HEAD", end="-->")
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end="-->")
            ptr = ptr.next
        print("NULL")

    def delete(self, ele):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == ele:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr is not None:
            if curr.data == ele:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print("Element not found")


print("Hi")

s = SingleLinkedList()

while True:
    op = int(input("1 Add, 2 Show, 3 Remove, 4 Exit: "))

    if op == 1:
        ele = input("Enter element: ")
        s.insert(ele)

    elif op == 2:
        s.show()

    elif op == 3:
        ele = input("Enter element to remove: ")
        s.delete(ele)

    elif op == 4:
        print("Bye")
        break

    else:
        print("Invalid option")1
        