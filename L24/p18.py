class Person:
    def __init__(self, id, name):
        self.id=id
        self.name = name

    def show(self):
        print("id=",self.id)
        print("name =",self.name)

class Teacher(Person):
    def __init__(self, id , name , salary):
        super().__init__(id,name)
        self.salary=salary

    def show(self):
        super().show()
        print("salary= ",self.salary)

class Hod(Teacher):
    def __init__(self, id ,name ,salary , dept):
        super().__init__(id,name,salary)
        self.dept=dept

    def show(self):
        super().show()
        print("Dept= ",self.dept)

h = Hod(101,"Soham",75000,"CSE")
h.show()