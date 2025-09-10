list1=[]
n=int(input("Enter number of elements in lists: "))
print("Enter the elements of list: ")
for i in range(n):
    list1.append(input())
print("List is: ",list1)
max=list1[0]
sec_max = list1[0]
for ele in list1:
    if(ele>max):
        sec_max=max
        max=ele
    elif ele > sec_max and ele != max:
        sec_max = ele
print("second maximum element is: ",sec_max)