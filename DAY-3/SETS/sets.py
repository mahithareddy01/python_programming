s=set()
n=int(input("Enter no. of elements to add: "))
print("Enter elements to add: ",end="")
for i in range(n):
    i=input()
    s.add(i)

print(f"set is {s}")