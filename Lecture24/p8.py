#wapp to know area and circumference od f the circle

class Circle:
    def __init__(self,n):
        self.n=n

    def show(self):
        print("Radius =",self.n)

    def area(self):
        area= 3.14* self.n**2
        print("area = ",area)

    def circumference(self):
        circumference =2*3.14*self.n
        print("Circumference = ",circumference)

Radius =float(input("Enter the Radius of the circle: "))

s=Circle(Radius)
s.show()
s.area()
s.circumference()
