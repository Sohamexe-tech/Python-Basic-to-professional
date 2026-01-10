#waoopp for the rectangle 

class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def show(self):
        print("self= ",self)
        print("Length = ",self.l)
        print("breadth = ",self.b)

    def area(self):
        area=self.l*self.b
        print("Area of Reactangle: ",area)

    def perimeter(self):
        area=2*(self.l+self.b)
        perimeter=("perimeter of Reactangle: ",area)

l=float(input("Enter the length of the rectangle= "))
b=float(input("Enter the breadth of the rectangle= "))

r=rectangle(l,b)
r.show()
r.area()
r.perimeter()




