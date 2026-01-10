#OOP

class EvenOdd:
    def __init__(self,n):
        self.n= n

    def show(self):
        print("num: ", self.n)

    def check(self):
        if self.n%2==0:
            print("Even")
        else:
            print("Odd")

num = int(input("Enter Integer: "))
e = EvenOdd(num)
e.show()
e.check()