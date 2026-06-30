 #wamdoop for DS: Stack

class Stack:
    def __init__(self):
        self.data=[]

    def push(self,ele):
        self.data.append(ele)

    def pop(self):
        if len(self.data)==0:
            return"stack is empty"
        else:
            return self.data.pop()
              
    def show(self):
        print(self.data)

s = Stack()
while True:
    op = int(input("1 Push , 2 Pop, 3 Show,4 exit,\nEnter your choice:"))
    if op == 1:
        ele = input("Enter element to push:")
        s.push(ele)
    elif op == 2:
        print(s.pop())
    elif op == 3:
        s.show()
    elif op == 4:
        break   
    else:
        print("Invalid option")
