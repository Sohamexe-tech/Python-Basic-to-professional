class Stack:
        def __init__(self):
                self.data=[]

        def push(self,ele):
                self.data.append(ele)

        def pop(self):
                if len(self.data)==0:
                        return"Stack is Empty"
                else:
                        return self.data.pop()
                
        def show(self):
                print(self.data)

s=Stack()

while True: 
        op=int(input("1.Push , 2.POP , 3.View , 4.Exit \n"))
        if op==1:
                ele=input("Enter Element: ")
                s.push(ele)
        elif op==2:
                print(s.pop())
        elif op==3:
                s.show()
        elif op==4:
                break
        else:
                print("Inavlid option 1")