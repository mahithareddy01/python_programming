def print_unique(lst):
    res=[]
    for ele in lst:
        if(lst.count(ele)==1):
            res.append(ele)
    return res



lst=[]
n=int(input("Enter number of elements in list:  "))
print("Enter the elements of list: ")
for i in range(n):
    lst.append(input())
print("List is: ",lst)
print(f"unique elements in list : {print_unique(lst)}")