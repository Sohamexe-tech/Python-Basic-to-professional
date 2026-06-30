#OOP
class SquareRoot:
    def __init__(self,num):
        self.num = num
    
    def show(self):
        print("num = ",self.num)

    def sqrt(self):
        if self.num >= 0:
            ans = self.num ** 0.5
            print("sqrt =", round(ans, 2))
        else:
            print("Please enter positive number only")

try:
    num = float(input("Enter Number: "))
    s= SquareRoot(num)
    s.show()
    s.sqrt()
except ValueError:
    print("Please enter Number only")