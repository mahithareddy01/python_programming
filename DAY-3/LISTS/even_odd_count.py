def count(list):
    ecount=0
    ocount=0
    for ele in list:
        if(ele%2==0):
            ecount+=1
        else:
            ocount+=1
    return ecount,ocount
list=[]
n=int(input("Enter number of elements in lists: "))
print("Enter the elements of list: ")
for i in range(n):
    list.append(int(input()))
print("List is: ",list)
print(f"even and odd count:{count(list)} ")