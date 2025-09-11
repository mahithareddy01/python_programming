class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("-----STUDENT DETAILS-----")
        print(f"Name: {self.name}\nRoll Number: {self.roll_no}\nMarks: {self.marks}")

n=int(input("Enter number of students: "))
students=[]
for i in range(n):
    print(f"Enter details of student {i+1}--")
    name=input(f"Enter name of student {i+1} : ")
    roll=input(f"Enter roll Number of student {i+1} :")
    marks=input(f"Enter marks of the student {i+1}: ")
    print()
    s=Student(name,roll,marks)
    students.append(s)
for stu in students:
    stu.display()