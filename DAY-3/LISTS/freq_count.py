def frequency_count(lst):
    dict={}
    for ele in lst:
        dict[ele]=lst.count(ele)
    return dict

list1=[]
n=int(input("Enter number of elements in lists: "))
print("Enter the elements of list: ")
for i in range(n):
    list1.append(int(input()))
print("list is: ",list1)
print(f"The frequency count: {frequency_count(list1)}")