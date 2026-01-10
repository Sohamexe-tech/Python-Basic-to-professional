class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def show(self):
        print("Id :", self.id)
        print("Name :", self.name)
        print("Salary :", self.salary)


class TS(Employee):
    def __init__(self, id, name, salary, HRA, DA, TA):
        super().__init__(id, name, salary)
        self.HRA = HRA
        self.DA = DA
        self.TA = TA
        self.Totsalary = salary + HRA + DA + TA

    def show(self):
        super().show()
        print("HRA :", self.HRA)
        print("DA :", self.DA)
        print("TA :", self.TA)
        print("Total Salary :", self.Totsalary)


e = Employee(1, "SOHAM", 20000)
e.show()



t = TS(1, "SOHAM", 20000, 1000, 1660, 1000)
t.show()
