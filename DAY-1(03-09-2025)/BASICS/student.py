''' enter student number,
    student name,
    3 subject marks
    calculate total and average of student,print all stu details '''
n = int(input("Enter number of students: "))
name=[]
roll=[]
avg=[]
for i in range(n):
    print("Enter details of student ",i+1)
    name_input=input("Enter name of the student:")
    roll_input=input("Enter roll number of the student:")
    sub1=int(input("marks in math(subject 1):"))
    sub2=int(input("marks in physics(subject 2):"))
    sub3=int(input("marks in chemistry(subject 3):"))
    avg_curr=(sub1+sub2+sub3)/3
    name.append(name_input)
    roll.append(roll_input)
    avg.append(avg_curr)
    print("average of student ",i+1,"is : ",round(avg_curr,2))
print()
print("-----STUDENT DETAILS------")
for i in range(n):
    print("STUDENT--",i+1)
    print("Name of the student: ",name[i])
    print("Roll number of the student: ",roll[i])
    print("Average marks of the student: ",round(avg[i], 2))