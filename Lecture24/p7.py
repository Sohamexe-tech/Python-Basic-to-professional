#oop squroot finder

class SqureRoot:
    def __init__(self,n):
        self.n=n

    def show(self):
        print("num= ", self.n)

    def Sqrt(self):
        res= self.n**0.5
        print("Squre root= ",res)

num = float(input("Enter number: "))

s=SqureRoot(num)
s.show()
s.Sqrt()

