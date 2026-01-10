class Student:
    def __init__(self, rno, name, marks):
        self.rno = rno
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks > 80 and self.marks <= 100:
            return "A"
        elif self.marks > 60:
            return "B"
        elif self.marks >= 0:
            return "C"
        else:
            return "Invalid Marks"

    def show(self):
        print("Roll No :", self.rno)
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Grade   :", self.grade())


rno = input("Enter Roll No: ")
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))

s = Student(rno, name, marks)
s.show()
