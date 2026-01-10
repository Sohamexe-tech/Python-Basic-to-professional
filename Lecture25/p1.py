# single level inheritance

class Person:
        def __init__(self,id,name,address):
            self.id= id
            self.name= name
            self.address= address
        def show(self):
                print("Id :",self.id)
                print("Name :",self.name)
                print("Address :",self.address)

class Student(Person):
        def __init__(self,id,name,address,marks):
                super().__init__(id,name,address)
                self.marks= marks
        def show(self):
                super().show()
                print("Marks: :",self.marks)
                
p=Person(10,"Soham","Thane")
p.show()

s=Student(20,"Osho","MUMBAI",20)
s.show()


