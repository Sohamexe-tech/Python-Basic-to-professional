#wamdoopp for Linear DS : Queue -> FIFO

class Queue:
    def __init__(self):
        self.data= []

    def enq(self,ele):
        self.data.append(ele)
        print(ele," Is Inserted in the Queue")

    def deq(self):
        if len(self.data)==0:
            return "Queue is empty"
        else:
            return self.data.pop(0)
        
    def show(self):
        print(self.data)

print("hi")
q = Queue()
while True:
    op = int(input("1 Enqueue, 2 Dequeue , 3 Show , 4 Exit \n Enter Your Choice:"))
    if op==1:
        ele=int(input("Enter Integer: "))
        q.enq(ele)
    elif op==2:
        print(q.deq())
    elif op==3:
        q.show()
    elif op==4:
        print("bye")
        break
    else:
        print("Invalid Option")