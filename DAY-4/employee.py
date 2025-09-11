class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary=salary
    def display(self):
        print("----EMPLOYEE DETAILS----")
        print(f"Employee name: {self.name}\nEmployee salary: {self.salary}")
class Manager(Employee):
    def __init__(self,name,sal,dept):
        super().__init__(name,sal)
        self.dept=dept
    def display(self):
        super().display()
        print(f"Department name: {self.dept}")

nme=input("Enter Employee name: ")
sal=input("Enter Employee Salary: ")
dept=input("Enter department name: ")
emp=Employee(nme,sal)
emp.display()
manager=Manager(nme,sal,dept)
manager.display()
