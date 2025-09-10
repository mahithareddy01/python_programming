list=[]
n=int(input("Enter number of elements in lists: "))
print("Enter the elements of list: ")
for i in range(n):
    list.append(int(input()))
print("List is: ",list)
for ele in list[:]:
    if ele<0:
        list.remove(ele)
print("After removing negative values,list is: ",list)