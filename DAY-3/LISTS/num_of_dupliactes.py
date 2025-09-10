def duplicates(lst):
    cnt=0
    for ele in lst:
        while(lst.count(ele)>1):
            lst.remove(ele)
            cnt+=1
    return cnt

list1=[]
n=int(input("Enter number of elements in list: "))
print("Enter the elements of list: ")
for i in range(n):
    list1.append(int(input()))
print("list is: ",list1)
print(f"number of duplicates in list: {duplicates(list1)}")
