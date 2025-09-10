def duplicates(lst):
    for ele in lst:
        while(lst.count(ele)>1):
            lst.remove(ele)
    return lst

list1=[]
n=int(input("Enter number of elements in list: "))
print("Enter the elements of list: ")
for i in range(n):
    list1.append(int(input()))
print("list is: ",list1)
print(f"list after removing duplicates: {duplicates(list1)}")