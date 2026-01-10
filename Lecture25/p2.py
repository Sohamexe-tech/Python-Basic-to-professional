# single multilevel inheritance

class Person:
        def __init__(self,id,name,address):
            self.id= id
            self.name= name
            self.address= address
        def show(self):
                print("Id :",self.id)
                print("Name :",self.name)
                print("Address :",self.address)

class Teacher(Person):
        def __init__(self,id,name,address,salary):
                super().__init__(id,name,address)
                self.salary= salary
        def show(self):
                super().show()
                print("Salary: :",self.salary)

class HOD(Teacher):
        def __init__(self,id,name,address,salary,dept):
                super().__init__(id,name,address,salary)
                self.dept= dept
        def show(self):
                super().show()
                print("Department: :",self.dept)

p=Person(10,"Soham","Thane")
p.show()

t=Teacher(20,"Osho","MUMBAI",200000)
t.show()

h=HOD(20,"Jeffery","Epstein Island",200000,"pdf")
h.show()



