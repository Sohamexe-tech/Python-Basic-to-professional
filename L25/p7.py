#wamdoopp for linear DS : Stack -> LIFO
#FIFO-> First In Last Out

class Stack:
    def __init__(self):
        self.data=[]

    def push(self,ele):
        self.data.append(ele)
        print(ele," is Pushed on Stack")
    
    def pop(self):
        if len(self.data)==0:
            return"Stack is Empty"
        else:
            return self.data.pop()
        
    def show(self):
        print(self.data)

s=Stack()

print("Hi")
while True:
    op = int(input("1 Push, 2 Pop , 3 Show , 4 Exit \n Enter Your Choice:"))
    if op==1:
        ele=int(input("Enter Integer: "))
        s.push(ele)
    elif op==2:
        print(s.pop())
    elif op==3:
        s.show()
    elif op==4:
        print("bye")
        break
    else:
        print("Invalid Option")