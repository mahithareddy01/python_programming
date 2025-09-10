def remove(lst,pos):
    #list.pop(pos)
    res=[]
    p=0
    for ele in lst:
        if p==pos:
            p+=1
            continue
        res.append(ele)
        p+=1
    return res
list1=[]
n=int(input("Enter number of elements in lists: "))
print("Enter the elements of list: ")
for i in range(n):
    list1.append(input())
print("List is: ",list1)
idx=int(input("Enter an index to remove element: "))
print(f"After removing element at index {idx} , list : {remove(list1,idx)}")