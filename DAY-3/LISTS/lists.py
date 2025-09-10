lst=[]
n=int(input("Enter number of elements in list:  "))
print("Enter the elements of list: ")
for i in range(n):
    lst.append(input())
print("List is: ",lst)
#append,insert methods
a=int(input("enter an element to add: "))
lst.append(a) #adds at end
print("list: ",lst)
b=input("enter an element to add at index 2: ")
lst.insert(2,b)
print("list: ",lst)
#delete,pop,remove methods
print("removing element (at end): ")
print("removed: ",lst.pop())
print("now, list is: ",lst)
c=int(input("enter an element to remove at pos(using pop): "))
print(f"After removing element at {c} i.e {lst.pop(c)} , list is: {lst}")

d=input("Enter an element to remove:")
lst.remove(d)
print(f"after removing {d} , the list is: {lst}")