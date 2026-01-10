#OOP

class Square:
    def __init__(self,n):
        self.n= n
    
    def show(self):
        print("num = ", self.n)

    def square(self):
        res = self.n**2
        print("sqaur= ",res)

num = float(input("Enter Number: "))
s=Square(num)
s.show()
s.square()