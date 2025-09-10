def highest(stud):
    max=stud[0]
    for s in stud[1:]:
        if s[2]>max[2]:
            max=s
    return max
def above_75(stud):
    l=[]
    for s in stud:
        if s[2]>75:
            l.append(s[1])
    return l
lst=[]
n=int(input("Enter number of students: "))
print("Enter student details: ")
for i in range(n):
    roll=(input("Enter roll num of the student: "))
    name=(input("Enter name of the student: "))
    marks=int(input("Enter marks of the student: "))
    print()
    lst.append((roll,name,marks))
print(f"Student details(roll no,name,marks): {lst}")
print(f"Students with above 75 marks : {above_75(lst)}")
print(f"Student with highest marks: {highest(lst)}")