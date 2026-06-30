class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def show(self):
        print("id=",self.id)
        print("name =",self.name)

class Student(Person):
    def __init__(self,id,name,marks):
        super().__init__(id,name)
        self.marks = marks
    def show(self):
        super().show()
        print("Marks= ", self.marks)
    
    p=Person(10,"Soham")
    p.show()
s = Student (20,"Nimish",50)
s.show()
