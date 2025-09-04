def fibb(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibb(n-1)+fibb(n-2)
n=int(input("Enter a number: "))
print(f"Fibonacci series upto {n} terms is:")
for i in range(0,n+1):
    print(fibb(i),end=" ")