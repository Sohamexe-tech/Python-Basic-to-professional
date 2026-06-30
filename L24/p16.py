# wooop for class
# state
# behavior

class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def show(self):
        print("id =", self.id)
        print("name =", self.name)
        print("salary =", self.salary)

    def computeTax(self):
        if self.salary > 50000:
            amt = self.salary * 0.10
        else:
            amt = self.salary * 0.05

        print("tax amt =", amt)


try:
    id = int(input("Enter emp id: "))
except ValueError:
    print("Invalid emp id")
    exit()

if id <= 0:
    print("Emp id should be min 1")
    exit()


name = input("Enter name: ")

if name == "":
    print("Name cannot be empty")
    exit()

if not name.replace(" ", "").isalpha():
    print("Name should contain only alphabets")
    exit()


try:
    salary = float(input("Enter emp salary: "))
except ValueError:
    print("Invalid salary")
    exit()

if salary < 12000:
    print("Salary should be min 12K")
    exit()


e = Employee(id, name, salary)
e.show()
e.computeTax()
