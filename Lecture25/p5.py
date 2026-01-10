class Queue:
    def __init__(self):
            self.data=[]

    def enqueue(self,ele):
          self.data.append(ele)

    def dequeue(self):
          if len(self.data)==0:
                return"Queue is Empty"
          else:
                return self.data.pop(0)
          
    def show(self):
          print(self.data)

q=Queue()
while True:
            op=int(input("1. Enqueue, 2.Dequeue, 3.Show , 4. Exit \n"))
            if op==1:
                ele=input("Enter Element: ")
                q.enqueue(ele)
            elif op==2:
                print(q.dequeue())
            elif op==3:
                q.show()
            elif op==4:
                break
            else:
                print("Inavlid option 1")

        
    